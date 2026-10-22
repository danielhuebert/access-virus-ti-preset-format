#!/usr/bin/env python3
"""Byte-exact single-dump layout from the gearmulator JSON (midipackets).

Under 'midipackets' the JSON defines the packets 'singledump' (TI, 524 B) and
'singledump_C' (classic, 267 B) as a list with ONE entry per message byte.
This is the authoritative, complete byte->parameter mapping - no page guesswork.

Verified against 630 real TI dumps (enum consistency 83/85 = 97.6 %).
It also confirms the checksum: entry {"type":"checksum","first":5,"last":521}.

Entry types: byte (fixed value), deviceid, bank, program, param (named),
checksum, null, f7.
"""
import os
import re
import json

HERE = os.path.dirname(os.path.abspath(__file__))
TI_JSON = os.path.join(HERE, "..", "reference", "parameterDescriptions_TI.json")

from load_param_descriptions import _clean_jsonc, load_descriptions  # noqa: E402


def _get_midipackets(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r'"midipackets"\s*:', text)
    i = text.index("{", m.end())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(_clean_jsonc(text[i:j + 1]))
    raise ValueError("midipackets not found")


def dump_layout(packet="singledump", path=TI_JSON):
    """List: message_position -> entry dict (type, plus name/value where present)."""
    return _get_midipackets(path)[packet]


def position_names(packet="singledump", path=TI_JSON):
    """message_position -> parameter name (only 'param' entries)."""
    return {k: e["name"] for k, e in enumerate(dump_layout(packet, path))
            if e.get("type") == "param"}


def param_ranges(path=TI_JSON):
    """parameter name -> (min, max)."""
    params, _, _ = load_descriptions(path)
    return {p["name"]: (p["min"], p["max"]) for p in params}


# Which packet per dump length:
PACKET_BY_LENGTH = {524: "singledump", 267: "singledump_C"}


if __name__ == "__main__":
    import sys
    pkt = sys.argv[1] if len(sys.argv) > 1 else "singledump"
    names = position_names(pkt)
    rng = param_ranges()
    print(f"{pkt}: {len(names)} named parameter bytes\n")
    for pos in sorted(names):
        nm = names[pos]
        lo, hi = rng.get(nm, ("?", "?"))
        print(f"  msg[{pos:3d}] (data {pos - 9:3d})  {nm:<30} {lo}..{hi}")
