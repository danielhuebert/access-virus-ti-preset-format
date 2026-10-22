#!/usr/bin/env python3
"""Load the parameterdescriptions from the Osirus/OsTIrus JSONs (dsp56300/gearmulator).

The files are JSONC (comments, trailing commas) and the 'valuelists' section contains
single-quoted entries that are not valid JSON. We therefore extract only the
'parameterdescriptions' array by bracket matching and parse just that.

Each entry: {page, index, name, min, max, toText, isPublic, isDiscrete, isBool}

Mapping onto single-dump data offsets (confirmed against user banks):
    page == PAGE_A_VALUE  -> data_offset = index          (Page A, 0..127)
    page == PAGE_B_VALUE  -> data_offset = 128 + index     (Page B, 128..255)
    other pages (C/Multi/Global) do not appear in the single dump.
"""
import json
import re
import os


def _extract_array(text, key):
    m = re.search(r'"%s"\s*:' % re.escape(key), text)
    if not m:
        raise ValueError("key %r not found" % key)
    i = text.index("[", m.end())
    depth = 0
    for j in range(i, len(text)):
        c = text[j]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                return text[i:j + 1]
    raise ValueError("end of array not found")


def _clean_jsonc(s):
    s = re.sub(r'//[^\n]*', '', s)
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
    s = re.sub(r',(\s*[}\]])', r'\1', s)
    return s


# Single-dump pages for the classic 256-byte region (verified against user banks,
# 86.8 % value-range consistency, clearly the best pair). Valid for C AND TI dumps,
# since their first 256 data bytes are laid out identically.
# NOTE: in the TI JSON, 110/111 (0x6E/0x6F) are the parameter *change* pages, NOT the
# single dump. For the offset map, use the C JSON with 112/113.
SINGLE_DUMP_PAGE_A = 112
SINGLE_DUMP_PAGE_B = 113


def load_descriptions(path):
    """Return (parameter_list, pageA, pageB)."""
    text = open(path, encoding="utf-8").read()
    arr = _clean_jsonc(_extract_array(text, "parameterdescriptions"))
    params = json.loads(arr)
    return params, SINGLE_DUMP_PAGE_A, SINGLE_DUMP_PAGE_B


def build_offset_map(path):
    """data_offset (0..255) -> parameter dict, Page A/B only."""
    params, pageA, pageB = load_descriptions(path)
    offmap = {}
    for p in params:
        if p["page"] == pageA:
            off = p["index"]
        elif p["page"] == pageB:
            off = 128 + p["index"]
        else:
            continue
        if 0 <= off <= 255:
            offmap[off] = p
    return offmap, pageA, pageB


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    offmap, a, b = build_offset_map(path)
    print(f"{os.path.basename(path)}: Page A={a}, Page B={b}, {len(offmap)} single-dump parameters")
    for off in sorted(offmap):
        p = offmap[off]
        page = "A" if off < 128 else "B"
        print(f"  data[{off:3d}] {page}[{off % 128:3d}]  {p['name']:<24} {p['min']}..{p['max']}")
