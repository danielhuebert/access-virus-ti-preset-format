#!/usr/bin/env python3
"""Generate a small test bank to verify encode.py on a real Virus TI.

Three slots, derived from patch 0 of a source bank:
  Slot 0  'MR BASSSEQ'  -> original, byte-identical (reference: roundtrip)
  Slot 1  'CLAUDEDARK'  -> only Cutoff lowered to 20 (clearly darker, audible)
  Slot 2  'CLAUDEOPEN'  -> only renamed, sound unchanged (isolates the name path)

Usage: python3 -I src/make_device_test.py
Output: out/virus-ti-encode-test.mid
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_sysex import parse_smf, classify, validate_single  # noqa: E402
from encode import Single, write_mid  # noqa: E402

SRC = os.path.join(HERE, "..", "samples", "Vengeance_Incubation_v5.mid")
OUTDIR = os.path.join(HERE, "..", "out")
OUT = os.path.join(OUTDIR, "virus-ti-encode-test.mid")


def main():
    msgs, _, _ = parse_smf(open(SRC, "rb").read())
    dumps = [m for m in msgs if classify(m)[1] == 0x10 and validate_single(m)[0]]
    base = dumps[0]

    ref = Single.from_message(base)
    ref.program = 0

    dark = Single.from_message(base)
    dark.program = 1
    dark.set("Cutoff", 20)
    dark.set_name("CLAUDEDARK")

    openp = Single.from_message(base)
    openp.program = 2
    openp.set_name("CLAUDEOPEN")

    singles = [ref, dark, openp]
    os.makedirs(OUTDIR, exist_ok=True)
    write_mid(singles, OUT)

    # self-check
    m2, _, _ = parse_smf(open(OUT, "rb").read())
    d2 = [m for m in m2 if classify(m)[1] == 0x10 and validate_single(m)[0]]
    print("written:", OUT, "(%d bytes)" % os.path.getsize(OUT))
    print("patches:", len(d2), "| all checksums valid:", all(validate_single(m)[0] for m in d2))
    print("slot 0 byte-identical to original:", d2[0] == base)
    s2 = [Single.from_message(m) for m in d2]
    for i, s in enumerate(s2):
        print(f"  slot {i}: {s.name()!r:<14} Cutoff={s.get('Cutoff')}")


if __name__ == "__main__":
    main()
