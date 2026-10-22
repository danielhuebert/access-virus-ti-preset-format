# access-virus-ti-preset-format

Tools and a byte-level specification for the **Access Virus TI preset format** — read,
edit and write preset banks exported from Virus Control / Control Center.

The format is fully reverse-engineered for reading **and** writing, and the write path has
been verified on real Virus TI hardware.

## What it does

- Parse `.mid` preset banks (Standard MIDI Files that wrap the device's SysEx dumps).
- Decode every patch into **named parameters with human-readable values**
  (e.g. `Filter1 Mode = Low Pass`, `Osc1 Semitone = -24`).
- Edit patches (by raw value or by display text) and write valid banks back as `.mid` or `.syx`,
  with correct checksums.

Pure Python standard library, no dependencies.

## Format in a nutshell

```
.mid (SMF container)
  └── MIDI SysEx events
        └── Access SysEx single dumps   <- one per patch, the actual payload
```

A bank is a sequence of single dumps (`cmd 0x10`), one SysEx event per patch — there is no
enclosing bank message. Two dump variants exist:

| Variant | Header | Device | Total | Data bytes |
|---------|--------|--------|-------|------------|
| Classic | `F0 00 20 33 01 00 10` | `0x00` | 267 B | 256 (2 pages × 128) |
| Full TI | `F0 00 20 33 01 10 10` | `0x10` | 524 B | 513 (pages A/B + TI extension) |

Message layout: `F0 00 20 33 01 <dev> 10 <bank> <prog>  <data…>  <chk> F7`

- **Checksum**: `sum(bytes[5 .. last data byte]) & 0x7F`
- **Patch name**: 10 ASCII chars at data offset 240 (`SingleName0..9`)
- Full byte→parameter map comes from the gearmulator JSON (see [`reference/`](reference/)),
  cross-checked against ~1000 real patches.

The complete specification is in [docs/format.md](docs/format.md).

## Usage

```sh
# list all patch names in a bank
python3 -I src/decode.py "samples/Bank.mid"

# decode one patch into named parameters (human-readable values)
python3 -I src/decode.py "samples/Bank.mid" 0

# byte-exact roundtrip self-test (read in -> write back -> compare)
python3 -I src/encode.py "samples/Bank.mid"
```

Editing in code:

```python
from encode import Single, write_mid
from extract_sysex import parse_smf, classify, validate_single

msgs, _, _ = parse_smf(open("samples/Bank.mid", "rb").read())
dumps = [m for m in msgs if classify(m)[1] == 0x10 and validate_single(m)[0]]

patch = Single.from_message(dumps[0])
patch.set_text("Filter1 Mode", "High Pass")   # by display text
patch.set_text("Osc1 Semitone", "+12")         # bipolar
patch.set("Cutoff", 20)                          # by raw value
patch.set_name("MY PATCH")
write_mid([patch], "out/edited.mid")
```

## Layout

- `src/` — tools:
  - `extract_sysex.py` — SMF → SysEx + validation (length + checksum)
  - `decode.py` — bank → patch names + named parameters
  - `encode.py` — write patches back to `.mid` / `.syx` (`Single` class)
  - `dump_layout.py` — byte-exact dump layout from the gearmulator JSON
  - `value_text.py` — human-readable values (enums, bipolar, percent)
  - `load_param_descriptions.py`, `find_names.py`, `analyze_params.py` — helpers / research
  - `make_device_test.py` — build a small test bank for hardware verification
- `docs/format.md` — the byte-level specification
- `reference/` — vendored parameter tables from gearmulator (with source and licence)
- `samples/` — your own example banks (git-ignored; not committed)

## Credits & licence

Parameter names and value tables come from the open-source emulator
[**gearmulator**](https://github.com/dsp56300/gearmulator) (Osirus = Virus A/B/C,
OsTIrus = Virus TI) by "The Usual Suspects", GPLv3. The vendored JSON files in
[`reference/`](reference/) are unmodified; see [reference/README.md](reference/README.md).

This project is independent and not affiliated with or endorsed by Access Music.
"Access" and "Virus" are trademarks of their respective owners.
