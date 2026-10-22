#!/usr/bin/env python3
"""Decode Virus single dumps from a .mid bank into named parameters.

Uses the byte-exact dump layout from the gearmulator JSON (src/dump_layout.py):
- 524 B dumps -> packet 'singledump'   (Virus TI, incl. TI extension)
- 267 B dumps -> packet 'singledump_C' (classic A/B/C)
The patch name is the 10 bytes of the parameters SingleName0..9.

Usage:
    python3 -I src/decode.py "samples/Bank.mid"            # all patch names
    python3 -I src/decode.py "samples/Bank.mid" 0          # patch 0 in detail
    python3 -I src/decode.py "samples/Bank.mid" 0 --all    # include Undefined/empty bytes
"""
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_sysex import parse_smf, classify, validate_single  # noqa: E402
from dump_layout import position_names, param_ranges, PACKET_BY_LENGTH  # noqa: E402
from value_text import ValueFormatter  # noqa: E402

_NAME_CACHE = {}


def names_for(length):
    pkt = PACKET_BY_LENGTH.get(length)
    if pkt is None:
        return {}
    if pkt not in _NAME_CACHE:
        _NAME_CACHE[pkt] = position_names(pkt)
    return _NAME_CACHE[pkt]


def patch_name(msg):
    pos = names_for(len(msg))
    chars = []
    for p, nm in sorted(pos.items()):
        if nm.startswith("SingleName"):
            chars.append(chr(msg[p]) if 32 <= msg[p] < 127 else " ")
    return "".join(chars).rstrip()


def load_dumps(path):
    msgs, _, _ = parse_smf(open(path, "rb").read())
    return [m for m in msgs if classify(m)[1] == 0x10 and validate_single(m)[0]]


def main():
    path = sys.argv[1]
    which = None
    show_all = "--all" in sys.argv
    for a in sys.argv[2:]:
        if a.isdigit():
            which = int(a)

    dumps = load_dumps(path)
    if which is None:
        print(f"{len(dumps)} valid patches in {os.path.basename(path)}:\n")
        for i, m in enumerate(dumps):
            print(f"  [{i:3d}] {patch_name(m)!r}")
        return

    m = dumps[which]
    pos = names_for(len(m))
    vf = ValueFormatter()
    fmt = "TI (524 B)" if len(m) == 524 else "classic (267 B)"
    print(f"Patch [{which}] '{patch_name(m)}'  [{fmt}]\n")
    for p in sorted(pos):
        nm = pos[p]
        if nm.startswith("SingleName"):
            continue
        if not show_all and ("Undefined" in nm):
            continue
        val = m[p]
        print(f"  msg[{p:3d}] data[{p - 9:3d}]  {nm:<30} = {vf.format(nm, val)}")


if __name__ == "__main__":
    main()
