# Reference data (third-party)

## parameterDescriptions_C.json / parameterDescriptions_TI.json

Parameter descriptor tables from the open-source emulator **gearmulator**
(Osirus = Virus A/B/C, OsTIrus = Virus TI) by "The Usual Suspects".

- Repo: https://github.com/dsp56300/gearmulator
  (`source/axel/osirusJucePlugin/parameterDescriptions_C.json`,
   `source/axel/osTIrusJucePlugin/parameterDescriptions_TI.json`)
- Licence there: GPLv3 — these files are included unmodified, for reference only.

Each entry: `{page, index, name, min, max, toText, isPublic, isDiscrete, isBool}`.
The files also contain a `midipackets` section whose `singledump` / `singledump_C`
packets give the byte-exact dump layout (one entry per message byte), and a
`valuelists` section mapping raw values to display text.

**Important for the single-dump mapping (verified against own banks):**
- The decisive table is the **C JSON** with `page 112` = Page A (data 0..255) and
  `page 113` = Page B. `page 114` = Page C (multi/global, not in the single dump).
- In the **TI JSON**, `page 110/111` (0x6E/0x6F) are the parameter *change* pages, not the
  single dump — so do not use them for offset mapping. The TI JSON's `midipackets.singledump`
  packet is what unlocks the extra TI data bytes (dump length 524 instead of 267).
