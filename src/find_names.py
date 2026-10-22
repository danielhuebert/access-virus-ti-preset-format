#!/usr/bin/env python3
"""Find the patch name field in Virus single dumps.

Heuristic: the offset where, across ALL patches, 10 consecutive bytes are all
printable ASCII (and differ between patches) is the name field.

Usage: python3 -I src/find_names.py "samples/Bank.mid"
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_sysex import parse_smf, classify  # noqa: E402

NAME_LEN = 10


def printable(b):
    return 32 <= b < 127


def main():
    path = sys.argv[1]
    with open(path, "rb") as f:
        data = f.read()
    msgs, _, _ = parse_smf(data)
    dumps = [m for m in msgs if classify(m)[0] and classify(m)[1] == 0x10]
    if not dumps:
        print("No single dumps found.")
        return

    minlen = min(len(m) for m in dumps)
    print(f"{os.path.basename(path)}: {len(dumps)} dumps, min length {minlen}")

    # For every possible offset, check whether ALL dumps have 10 printable bytes there
    candidates = []
    for off in range(0, minlen - NAME_LEN):
        if all(all(printable(m[off + k]) for k in range(NAME_LEN)) for m in dumps):
            candidates.append(off)

    if not candidates:
        print("No continuously printable 10-byte window found across all dumps.")
        return

    print(f"Name candidate offsets: {candidates}")
    for off in candidates:
        names = [m[off:off + NAME_LEN].decode("latin-1").rstrip() for m in dumps[:12]]
        # only offsets with varying, sensible-looking names are of interest
        distinct = len(set(m[off:off + NAME_LEN] for m in dumps))
        print(f"\n  Offset {off} (from start, incl. F0): {distinct} distinct values")
        for i, n in enumerate(names):
            print(f"    [{i:3d}] {n!r}")


if __name__ == "__main__":
    main()
