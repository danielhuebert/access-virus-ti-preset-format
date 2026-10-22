#!/usr/bin/env python3
"""SMF (.mid) -> SysEx extractor for Access Virus TI preset banks.

Decompilation step 1: parse a Standard MIDI File, pull out every SysEx message
and analyse them. No dependencies (standard library only).

Usage:
    python3 -I src/extract_sysex.py "samples/Bank.mid" [--dump-dir out/]
"""
import sys
import os
import argparse
from collections import Counter

ACCESS_ID = bytes([0x00, 0x20, 0x33])


def read_varlen(data, i):
    """MIDI variable-length quantity. Returns (value, new_index)."""
    value = 0
    while True:
        b = data[i]
        i += 1
        value = (value << 7) | (b & 0x7F)
        if not (b & 0x80):
            break
    return value, i


def parse_smf(data):
    """Parse an SMF and return a list of all SysEx messages (bytes, incl. F0..F7)."""
    if data[:4] != b"MThd":
        raise ValueError("No MThd signature - not a Standard MIDI File")
    header_len = int.from_bytes(data[4:8], "big")
    fmt = int.from_bytes(data[8:10], "big")
    ntrks = int.from_bytes(data[10:12], "big")
    pos = 8 + header_len

    sysex_msgs = []
    for _ in range(ntrks):
        if data[pos:pos + 4] != b"MTrk":
            # Robust: find the next MTrk
            nxt = data.find(b"MTrk", pos)
            if nxt < 0:
                break
            pos = nxt
        trk_len = int.from_bytes(data[pos + 4:pos + 8], "big")
        pos += 8
        end = pos + trk_len
        i = pos
        running_status = None
        pending = None  # for SysEx split across events (F0 ... / F7 continuation)
        while i < end:
            _, i = read_varlen(data, i)  # delta time (ignored)
            status = data[i]
            if status == 0xFF:  # meta event
                i += 1
                _meta_type = data[i]
                i += 1
                length, i = read_varlen(data, i)
                i += length
            elif status == 0xF0:  # SysEx start
                i += 1
                length, i = read_varlen(data, i)
                chunk = data[i:i + length]
                i += length
                msg = bytes([0xF0]) + chunk
                if chunk and chunk[-1] == 0xF7:
                    sysex_msgs.append(msg)
                else:
                    pending = msg  # to be continued
            elif status == 0xF7:  # SysEx continuation or escape
                i += 1
                length, i = read_varlen(data, i)
                chunk = data[i:i + length]
                i += length
                if pending is not None:
                    pending += chunk
                    if chunk and chunk[-1] == 0xF7:
                        sysex_msgs.append(pending)
                        pending = None
                # otherwise: plain escape event, ignored
            else:  # channel voice/mode message (possibly running status)
                if status & 0x80:
                    running_status = status
                    i += 1
                # number of data bytes depends on the status type
                high = (running_status or status) & 0xF0
                nbytes = 1 if high in (0xC0, 0xD0) else 2
                i += nbytes
        pos = end
    return sysex_msgs, fmt, ntrks


def classify(msg):
    """Detect Access SysEx; return (is_access, command, bank, program)."""
    # F0 00 20 33 01 10 <cmd> ...
    if len(msg) >= 7 and msg[1:4] == ACCESS_ID:
        cmd = msg[6]
        bank = msg[7] if len(msg) > 7 else None
        prog = msg[8] if len(msg) > 8 else None
        return True, cmd, bank, prog
    return False, None, None, None


# Valid total lengths of a single dump (cmd 0x10): classic and full-TI respectively.
VALID_SINGLE_LENGTHS = (267, 524)


def checksum_ok(msg):
    """Check the Virus checksum: sum(bytes from device id to last data byte) & 0x7F."""
    if len(msg) < 4:
        return False
    return (sum(msg[5:-2]) & 0x7F) == msg[-2]


def validate_single(msg):
    """Return (ok, reason) for a single dump."""
    if len(msg) not in VALID_SINGLE_LENGTHS:
        return False, "unexpected length %d" % len(msg)
    if not checksum_ok(msg):
        return False, "bad checksum"
    return True, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("midifile")
    ap.add_argument("--dump-dir", default=None,
                    help="if set: write each SysEx message there as a .syx file")
    args = ap.parse_args()

    with open(args.midifile, "rb") as f:
        data = f.read()

    msgs, fmt, ntrks = parse_smf(data)
    print(f"File: {os.path.basename(args.midifile)}")
    print(f"SMF format {fmt}, {ntrks} track(s), {len(msgs)} SysEx messages\n")

    len_counter = Counter(len(m) for m in msgs)
    cmd_counter = Counter()
    access = 0
    for m in msgs:
        is_a, cmd, bank, prog = classify(m)
        if is_a:
            access += 1
            cmd_counter[cmd] += 1

    valid = sum(1 for m in msgs if classify(m)[1] == 0x10 and validate_single(m)[0])
    singles = sum(1 for m in msgs if classify(m)[1] == 0x10)
    print(f"Access SysEx: {access} / {len(msgs)}")
    print(f"Single dumps valid (length+checksum): {valid} / {singles}")
    print("Length distribution (bytes incl. F0..F7):")
    for ln, cnt in sorted(len_counter.items()):
        print(f"   {ln:5d} bytes  x{cnt}")
    print("\nCommand byte distribution (msg[6]):")
    for cmd, cnt in sorted(cmd_counter.items()):
        print(f"   0x{cmd:02X}  x{cnt}")

    # Show the first few Access dumps (header + possible ASCII name area)
    print("\nFirst 3 single-dump candidates (cmd=0x10):")
    shown = 0
    for m in msgs:
        is_a, cmd, bank, prog = classify(m)
        if is_a and cmd == 0x10:
            head = " ".join(f"{b:02X}" for b in m[:16])
            # ASCII preview of the whole payload
            ascii_preview = "".join(chr(b) if 32 <= b < 127 else "." for b in m)
            print(f"  len={len(m)} bank={bank} prog={prog}")
            print(f"    head: {head}")
            print(f"    ascii: {ascii_preview[:96]}")
            shown += 1
            if shown >= 3:
                break

    if args.dump_dir:
        os.makedirs(args.dump_dir, exist_ok=True)
        for idx, m in enumerate(msgs):
            with open(os.path.join(args.dump_dir, f"msg_{idx:03d}.syx"), "wb") as f:
                f.write(m)
        print(f"\n{len(msgs)} messages written to {args.dump_dir}.")


if __name__ == "__main__":
    main()
