#!/usr/bin/env python3
"""Write Virus TI single dumps: Patch -> SysEx -> .syx / .mid.

Inverse of decode.py. Works byte-oriented so the roundtrip
(read in -> write back) is provable bit-for-bit.

Dump layout (both variants):
    F0 00 20 33 01 <dev> 10 <bank> <prog>  <data...>  <chk> F7
    chk = sum(bytes[5 .. last data byte]) & 0x7F     (= JSON {checksum, first:5, last:-2})

Usage (demo/roundtrip test): python3 -I src/encode.py "samples/Bank.mid"
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_sysex import parse_smf, classify, validate_single, ACCESS_ID  # noqa: E402
from dump_layout import position_names, PACKET_BY_LENGTH  # noqa: E402
from value_text import ValueFormatter  # noqa: E402

_VF = None


def _formatter():
    global _VF
    if _VF is None:
        _VF = ValueFormatter()
    return _VF

PREFIX_LEN = 9          # F0 00 20 33 01 dev 10 bank prog
PRODUCT = 0x01
CMD_SINGLE = 0x10

_NAMEPOS = {}


def _name_to_pos(length):
    """parameter name -> message position for the given dump length."""
    pkt = PACKET_BY_LENGTH.get(length)
    if pkt is None:
        raise ValueError("unknown dump length %d" % length)
    if pkt not in _NAMEPOS:
        _NAMEPOS[pkt] = {nm: p for p, nm in position_names(pkt).items()}
    return _NAMEPOS[pkt]


def virus_checksum(msg_wo_chk_f7):
    """Checksum over bytes[5..end] of the message without chk+F7."""
    return sum(msg_wo_chk_f7[5:]) & 0x7F


class Single:
    """A single patch, held internally as data bytes (no header/checksum/F7)."""

    def __init__(self, data, device=0x10, bank=0x01, program=0x00):
        self.data = bytearray(data)          # data bytes only
        self.device = device
        self.bank = bank
        self.program = program

    @property
    def total_length(self):
        return PREFIX_LEN + len(self.data) + 2   # + chk + F7

    @classmethod
    def from_message(cls, msg):
        """Read from a complete SysEx message (F0..F7)."""
        if msg[1:4] != ACCESS_ID or msg[6] != CMD_SINGLE:
            raise ValueError("not an Access single-dump message")
        return cls(msg[PREFIX_LEN:-2], device=msg[5], bank=msg[7], program=msg[8])

    def to_message(self):
        """Build the complete SysEx message (F0..F7) with a correct checksum."""
        body = bytearray([0xF0, 0x00, 0x20, 0x33, PRODUCT,
                          self.device & 0x7F, CMD_SINGLE,
                          self.bank & 0x7F, self.program & 0x7F])
        body += self.data
        body.append(virus_checksum(body))
        body.append(0xF7)
        return bytes(body)

    # --- named parameter access ---
    def _pos(self, name):
        return _name_to_pos(self.total_length)[name]

    def get(self, name):
        return self.data[self._pos(name) - PREFIX_LEN]

    def set(self, name, value):
        if not 0 <= value <= 127:
            raise ValueError("value %r outside 0..127" % value)
        self.data[self._pos(name) - PREFIX_LEN] = value

    def set_text(self, name, text):
        """Set a parameter by display text, e.g. set_text('Filter1 Mode', 'High Pass').

        Also accepts bipolar texts ('-24') and plain numbers."""
        self.set(name, _formatter().value(name, text))

    def get_text(self, name):
        """Human-readable value of this parameter ('text (raw)' or raw number)."""
        return _formatter().format(name, self.get(name))

    def name(self):
        pos = position_names(PACKET_BY_LENGTH[self.total_length])
        out = []
        for p, nm in sorted(pos.items()):
            if nm.startswith("SingleName"):
                c = self.data[p - PREFIX_LEN]
                out.append(chr(c) if 32 <= c < 127 else " ")
        return "".join(out).rstrip()

    def set_name(self, text):
        pos = position_names(PACKET_BY_LENGTH[self.total_length])
        slots = sorted(p for p, nm in pos.items() if nm.startswith("SingleName"))
        text = (text + " " * len(slots))[:len(slots)]
        for p, ch in zip(slots, text):
            self.data[p - PREFIX_LEN] = ord(ch) & 0x7F


# ---------------- output ----------------

def write_syx(singles, path):
    """Raw SysEx messages back to back (.syx)."""
    with open(path, "wb") as f:
        for s in singles:
            f.write(s.to_message())


def _varlen(n):
    out = bytearray([n & 0x7F])
    n >>= 7
    while n:
        out.insert(0, (n & 0x7F) | 0x80)
        n >>= 7
    return bytes(out)


def write_mid(singles, path, division=480):
    """Standard MIDI File (format 0) with one SysEx event per patch."""
    track = bytearray()
    for s in singles:
        msg = s.to_message()
        track += _varlen(0)                       # delta time
        track += bytes([0xF0]) + _varlen(len(msg) - 1) + msg[1:]  # F0 <len> <rest incl. F7>
    track += _varlen(0) + bytes([0xFF, 0x2F, 0x00])   # End of Track
    with open(path, "wb") as f:
        f.write(b"MThd" + (6).to_bytes(4, "big") +
                (0).to_bytes(2, "big") + (1).to_bytes(2, "big") +
                division.to_bytes(2, "big"))
        f.write(b"MTrk" + len(track).to_bytes(4, "big") + bytes(track))


# ---------------- roundtrip self-test ----------------

def _roundtrip_test(midpath):
    msgs, _, _ = parse_smf(open(midpath, "rb").read())
    dumps = [m for m in msgs if classify(m)[1] == CMD_SINGLE and validate_single(m)[0]]
    ok = 0
    for m in dumps:
        rebuilt = Single.from_message(m).to_message()
        if rebuilt == m:
            ok += 1
        else:
            print("  MISMATCH at prog", m[8])
    print("%s: %d/%d dumps written back byte-identical" %
          (os.path.basename(midpath), ok, len(dumps)))
    return ok, len(dumps)


if __name__ == "__main__":
    _roundtrip_test(sys.argv[1])
