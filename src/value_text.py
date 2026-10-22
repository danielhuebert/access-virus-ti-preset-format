#!/usr/bin/env python3
"""Human-readable parameter values for the Virus TI.

Every parameter in the gearmulator JSON has a `toText` field naming a value table in
the `valuelists` section. There index = raw value (0..127) and the entry is the display
text, e.g.:
    filter1Mode -> ["Low Pass","High Pass","Band Pass",...]
    signed      -> ["-64","-63",...,"63"]   (bipolar)
    oscWave     -> ["Sine","Triangle","Wave 3",...]
Empty `toText` or a value outside the table -> raw number.

Wired to the real dump layout via the parameter names from dump_layout.
"""
import os
import re
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TI_JSON = os.path.join(HERE, "..", "reference", "parameterDescriptions_TI.json")

from load_param_descriptions import _clean_jsonc, load_descriptions  # noqa: E402


def _extract_object(text, key):
    m = re.search(r'"%s"\s*:' % re.escape(key), text)
    if not m:
        raise ValueError("key %r not found" % key)
    i = text.index("{", m.end())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i:j + 1]
    raise ValueError("end of object not found")


def _fix_single_quotes(blob):
    """Single-quoted single characters ('x') -> valid JSON ("x")."""
    def repl(mm):
        c = mm.group(1)
        if c == "\\":
            return '"\\\\"'
        if c == '"':
            return '"\\""'
        return '"' + c + '"'
    return re.sub(r"'(\\?.)'", repl, blob)


def load_valuelists(path=TI_JSON):
    text = open(path, encoding="utf-8").read()
    blob = _fix_single_quotes(_clean_jsonc(_extract_object(text, "valuelists")))
    return json.loads(blob)


def load_totext(path=TI_JSON):
    """parameter name -> toText key."""
    params, _, _ = load_descriptions(path)
    return {p["name"]: p.get("toText", "") for p in params}


class ValueFormatter:
    def __init__(self, path=TI_JSON):
        self.lists = load_valuelists(path)
        self.totext = load_totext(path)
        self._reverse = {}   # toText key -> {normalised text: index}

    def _rev(self, key):
        """text -> index for a value table (first occurrence wins on duplicates)."""
        if key not in self._reverse:
            rv = {}
            lst = self.lists.get(key, [])
            items = lst.items() if isinstance(lst, dict) else enumerate(lst)
            for i, entry in items:
                norm = str(entry).strip().lower()
                rv.setdefault(norm, int(i))   # first occurrence wins
            self._reverse[key] = rv
        return self._reverse[key]

    def value(self, param_name, text):
        """Inverse of text(): display text -> raw value (0..127). Raises if unknown.

        Also accepts a number directly (as int or digit string)."""
        if isinstance(text, int):
            return text
        s = str(text).strip()
        if s.lstrip("+-").isdigit():
            # plain number: try as display text first (e.g. '-24' in 'signed'),
            # otherwise interpret as raw value
            key = self.totext.get(param_name, "")
            idx = self._rev(key).get(s.lower()) if key else None
            return idx if idx is not None else int(s)
        key = self.totext.get(param_name, "")
        if not key:
            raise ValueError(f"{param_name!r} has no value table - please give a number 0..127")
        idx = self._rev(key).get(s.lower())
        if idx is None:
            raise ValueError(f"{s!r} is not a valid value for {param_name!r} (table {key!r})")
        return idx

    def choices(self, param_name):
        """List of possible display texts (for discrete params), else None."""
        key = self.totext.get(param_name, "")
        lst = self.lists.get(key)
        if not key or key in ("ascii", "signed", "signedMidOff", "pan",
                              "biPolarPercent", "unipolarPercent", "unsignedZero"):
            return None
        # only offer genuine enums (short tables) as choices
        if isinstance(lst, dict):
            return [str(e).strip() for e in lst.values()] if len(lst) <= 32 else None
        if lst and len(lst) <= 32:
            return [str(e).strip() for e in lst]
        return None

    def text(self, param_name, raw):
        """Human-readable value, or None if no mapping applies."""
        key = self.totext.get(param_name, "")
        if not key or key == "ascii":
            return None
        lst = self.lists.get(key)
        if isinstance(lst, dict):
            v = lst.get(str(raw))
            return str(v).strip() if v is not None else None
        if lst and 0 <= raw < len(lst):
            return str(lst[raw]).strip()
        return None

    def format(self, param_name, raw):
        """Always a string: 'text (raw)' or just 'raw'."""
        t = self.text(param_name, raw)
        return f"{t} ({raw})" if t is not None else str(raw)


if __name__ == "__main__":
    f = ValueFormatter()
    for nm, raw in [("Filter1 Mode", 1), ("Cutoff", 64), ("Osc1 Wave Select", 0),
                    ("Reverb Type", 2), ("Patch Volume", 100), ("Osc1 Semitone", 69)]:
        print(f"  {nm:<18} raw={raw:3d} -> {f.format(nm, raw)}")
