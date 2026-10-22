#!/usr/bin/env python3
"""Empirical parameter map: which of the 256 data bytes (Page A/B) carry parameters?

Idea: across all valid single dumps of a bank, count how many distinct values occur per
data offset. Offsets with >1 value are active parameters; constant offsets are
unused/reserved or bank-wide identical. Purely data-driven, verifiable without a device.

Data region (identical for classic and TI across the first 256 bytes):
    data[d] = message[9 + d],  d = 0..255   (Page A = 0..127, Page B = 128..255)

Usage: python3 -I src/analyze_params.py "samples/Bank.mid" [more.mid ...]
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_sysex import parse_smf, classify, validate_single  # noqa: E402

DATA_START = 9        # message index of the first data byte
PAGE_SIZE = 128
NAME_OFF = 240        # data offset of the name (confirmed)
NAME_LEN = 10


def collect(paths):
    dumps = []
    for p in paths:
        data = open(p, "rb").read()
        msgs, _, _ = parse_smf(data)
        for m in msgs:
            if classify(m)[1] == 0x10 and validate_single(m)[0]:
                dumps.append(m)
    return dumps


def main():
    paths = sys.argv[1:]
    dumps = collect(paths)
    print(f"{len(dumps)} valid dumps from {len(paths)} file(s)\n")
    if not dumps:
        return

    # Per data offset 0..255: set of values
    sets = [set() for _ in range(256)]
    for m in dumps:
        for d in range(256):
            idx = DATA_START + d
            if idx < len(m) - 2:   # within the data (before chk+F7)
                sets[d].add(m[idx])

    active = [(d, len(s), min(s), max(s)) for d, s in enumerate(sets) if len(s) > 1]
    const = [d for d, s in enumerate(sets) if len(s) == 1]

    print(f"Active parameter offsets: {len(active)}  |  constant offsets: {len(const)}")
    print("\n--- PAGE A (0..127): active offsets (distinct / min / max) ---")
    for d, n, lo, hi in active:
        if d < PAGE_SIZE:
            print(f"  A[{d:3d}]  distinct={n:3d}  range {lo}..{hi}")
    print("\n--- PAGE B (128..255): active offsets ---")
    for d, n, lo, hi in active:
        if d >= PAGE_SIZE:
            tag = "  <- NAME" if NAME_OFF <= d < NAME_OFF + NAME_LEN else ""
            print(f"  B[{d - PAGE_SIZE:3d}] (data {d:3d})  distinct={n:3d}  range {lo}..{hi}{tag}")


if __name__ == "__main__":
    main()
