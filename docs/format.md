# Access Virus TI — preset format (specification / reverse engineering)

Working document. Goal: fully decompile the preset format, first reading, then writing.
Status: reading **and** writing done and verified on hardware.

## Format chain

The Virus TI transmits/stores presets as **SysEx**. The software (Virus Control /
Control Center) exports libraries as **`.mid`** — a Standard MIDI File (SMF) that wraps
the SysEx messages as MIDI SysEx events.

```
.mid (SMF container)
  └── MIDI SysEx events
        └── Access SysEx message(s)   <- the actual preset payload
```

Decompilation is therefore two-stage:
1. **Parse the SMF** → extract SysEx events (well-documented standard format).
2. **Decode the SysEx payload** → the unknown Access format (our focus).

`.syx` = the same SysEx messages raw, without the SMF wrapper. Convertible (TI Revive:
`tirevive-cc export FILE.mid OUT.syx`).

## Verified against own banks (2026-10-22)

Tools: [`src/extract_sysex.py`](../src/extract_sysex.py) (SMF→SysEx),
[`src/find_names.py`](../src/find_names.py) (name field). Banks from `samples/`.

**One `.mid` bank = N consecutive single dumps (cmd `0x10`), one SysEx event per patch.**
No enclosing bank message. `bb`=bank (here `0x01` = RAM A), `pp`=program `0..127`.

**Two dump variants** (distinguishable by the device byte `msg[5]` + length):

| Variant | Header                 | Device | Total length | Data bytes |
|---------|------------------------|--------|--------------|------------|
| Classic | `F0 00 20 33 01 00 10` | `0x00` | **267 B**    | 256 (= 2 pages × 128) |
| Full TI | `F0 00 20 33 01 10 10` | `0x10` | **524 B**    | 513 (pages A/B + TI extension) |

Layout: `F0 00 20 33 01 <dev> 10 bb pp  <data…>  <chk> F7`
(9-byte prefix + data + 1 checksum byte + `F7`).

**Patch name:** 10 ASCII chars from **message offset 249** = **data offset 240**,
identical in BOTH variants. (Matches the classic Virus layout: name at the end of page B.)
Verified: `Trilogy JL`, `WarmPad JL`, `UXB2 001`, …

Parsed banks:
- `Juho Lepisto SoundSet.mid` — 128× classic (267 B)
- `Ultimate X BASS Vol.2 …OS_5.0.3.00.mid` — 128× full TI (524 B)
- `VTG Electro Signature Set 2010.mid` — 118× full TI (524 B)
- `Incubation V3 … .mid` — **corrupt file**: 128 events, but only 31 valid. 97 patches are
  truncated in the middle (159/203 instead of 267 B), bad checksum → incomplete/corrupt dumps,
  not loadable onto the device. Head (0–175) and tail (name + `00 00 00 01 03 7F`) identical,
  middle parameter blocks missing. Not a format variant.
- `Matt Picone - Signature Set 2.mid` — 256× classic (= 2 banks in one file).
- `Patt Picone - Matman 2009.mid`, `Vengeance_Incubation_v5.mid`, `..._v5x.mid` — 128× full TI each, all valid.

**Validation status:** 1013/1110 single dumps valid across all banks; the only exception is
the corrupt V3 file. Rule: length ∈ {267, 524} **and** valid checksum.
Tool: `validate_single()` in [`extract_sysex.py`](../src/extract_sysex.py).

## Parameter map (complete, verified, 2026-10-22)

**Authoritative source:** the `midipackets` definitions in the gearmulator JSON
([`reference/parameterDescriptions_TI.json`](../reference/)). They contain the complete
dump as a list with **one entry per message byte**:
- `singledump`   → **TI, 524 B** (data bytes `msg[9..519]`, incl. TI extension)
- `singledump_C` → **classic, 267 B** (data bytes `msg[9..264]`)

Every data byte is thus directly mapped to a named parameter — no page guesswork needed.
Loader: [`src/dump_layout.py`](../src/dump_layout.py). A ready-made, browsable table of every
byte position (e.g. Cutoff = msg 49 / data 40) is in [`parameter-map.md`](parameter-map.md)
(regenerate with `python3 -I src/dump_layout.py`).

**Verification against 630 real TI dumps:** enum consistency **83/85 (97.6 %)**
(the 2 deviations harmless: "Delay Clock" 0..17 instead of 0..16; one always-0 default).
Additionally confirmed byte-exactly:
- **Checksum** = JSON entry `{"type":"checksum","first":5,"last":521}` → identical to
  our `sum(m[5:-2]) & 0x7F`.
- **Name** = parameters `SingleName0..9` at `msg[249..258]` = data 240..249 (matches our
  independent finding and the Infekted forum).

**Region breakdown of the TI dump (data offsets):**
- `0..~247`  : classic single (Osc1/2, Filter1/2, Cutoff@40, env, LFO, Patch Volume, …)
- `240..249` : patch name (10 ASCII)
- `~258..`   : **TI extension** — reverb (mode/type/time/damping/color/predelay/feedback),
  delay/tape delay, filter bank, character, osc wavetable/formant, soft knobs, …
- `data[512]`: trailer, always 0.

Decode a bank: [`src/decode.py`](../src/decode.py) → patch names + all named parameters
(both formats, chosen automatically by dump length).

## Known SysEx structure

Source: reverse-engineering project **TI Revive** (`findings/spec.md`, `evidence.md`).

| Element                  | Value / bytes                                   |
|--------------------------|-------------------------------------------------|
| Manufacturer ID (Access) | `00 20 33`                                      |
| SysEx header             | `F0 00 20 33 01 10` (product `01`, device `0x10`) |
| Single dump              | `10 bb pp …`  (`bb`=bank, `pp`=program; `bb 00` = edit buffer) |
| Single dump (observed)   | **524 bytes**, starts `10 00 00 …`              |
| Single dump request      | `30 bb pp`                                       |
| Multi/part parameter     | `72 pp ii vv`  (`ii 0x21` = program)            |
| Global parameter         | `73 pp ii vv`  (`ii 0x54` = Sync Information Event) |
| Parameter page C         | `6E pp ii vv`  (inferred)                        |
| Banks                    | RAM A–D, **128 patches** each                    |

Device handshake reply: `F0 00 20 33 01 10 73 40 40 00 F7`.
Identity Request `F0 7E 7F 06 01 F7` is standard (not Access-specific).

## Open questions (= decompilation tasks)

- [x] ~~Bank dump structure~~ → N single dumps, no enclosing message.
- [x] ~~Name field~~ → data offset 240, 10 ASCII chars (both variants).
- [x] ~~Checksum scheme~~ → **`chk = sum(bytes from device id (index 5) to last data byte) & 0x7F`**
      (= device + cmd + bank + prog + Σdata, mod 128). Verified over 364 dumps, both variants. Important for writing.
- [x] ~~Parameter addressing (all 511 data bytes)~~ → complete from gearmulator `midipackets`, verified.
- [x] ~~TI extension (data 256+)~~ → reverb/delay/filter bank/character/wavetable etc., mapped byte-exactly.
- [x] ~~Incubation V3 anomaly~~ → corrupt file (97/128 patches truncated).
- [x] ~~Human-readable values~~ → [`src/value_text.py`](../src/value_text.py): each parameter's `toText`
      points to a `valuelists` table (index = raw value → text). Bipolar (`signed`→ −64..63),
      enums (`filter1Mode`→ "Low Pass"…), `oscWave`, `reverbType`, percent, etc. Integrated in `decode.py`
      (shows "text (raw)"). Example: `Osc1 Semitone 40 → -24`, `Filter1 Mode 0 → Low Pass`.
- [x] ~~Set values by text~~ → `ValueFormatter.value()` (text→raw) + `Single.set_text()`/`get_text()`
      in `encode.py`. E.g. `set_text("Filter1 Mode","High Pass")`, `set_text("Osc1 Semitone","+12")`.
      Invalid values raise an error naming the table. `choices(name)` lists enum options.
- [ ] Name charset: mostly ASCII, occasional special chars (`@`) — charset table in the TI JSON `valuelists`.
- [x] ~~**Writing**~~ → [`src/encode.py`](../src/encode.py): `Single` class (named get/set, name,
      checksum), `write_syx()`, `write_mid()`. **Byte roundtrip 1045/1045 dumps identical**;
      end-to-end edit (change Cutoff+name → `.mid` → read back) produces valid checksums,
      leaves other patches byte-identical, output file same size as original.
- [x] ~~**Verified on hardware (2026-10-22)**~~: edited `.mid` (`src/make_device_test.py`) loaded via
      Virus Control — edited patch (Cutoff/name) correct, unchanged reference identical.
      Writing is therefore device-valid.

## Method for mapping offsets

1. Export a patch, change **one** parameter on the device, export again → byte diff shows
   that parameter's position. (Repeat systematically for every knob.)
2. Change the patch name → find the ASCII region in the dump (name offset + length).
3. Compare a single-patch dump vs. a bank dump → the bank's container structure.

## Sources

- TI Revive — reverse engineering (driver/protocol/format): https://github.com/spandthat/access-virus-ti-revive
  (relevant: `findings/spec.md`, `findings/evidence.md`, `findings/claims.md`)
- gearmulator (Osirus/OsTIrus) — parameter names, value tables, dump packet layout:
  https://github.com/dsp56300/gearmulator
- Access Virus MIDI/SysEx implementation (community guide, older model, for cross-checking)
