# Single-dump byte map

Generated from `reference/parameterDescriptions_TI.json` (`midipackets.singledump` / `singledump_C`) by `src/dump_layout.py`.

`msg` = byte index in the SysEx message (incl. F0), `data` = msg − 9 (after the 9-byte prefix `F0 00 20 33 01 dev 10 bank prog`).


## Full TI dump (524 bytes) — packet `singledump`

| msg | data | parameter | range | value type |
|----:|-----:|-----------|-------|------------|
| 9 | 0 | Version | 0..12 | version |
| 10 | 1 | Modulation Wheel | 0..127 |  |
| 11 | 2 | Breath Controller | 0..127 |  |
| 12 | 3 | Contr 3 | 0..127 |  |
| 13 | 4 | Foot Controller | 0..127 |  |
| 14 | 5 | Portamento Time | 0..127 | unsignedOff |
| 15 | 6 | Data Slider | 0..127 |  |
| 16 | 7 | Channel Volume | 0..127 |  |
| 17 | 8 | Balance | 0..127 |  |
| 18 | 9 | Contr 9 | 0..127 |  |
| 19 | 10 | Panorama | 0..127 | panPercent |
| 20 | 11 | Expression | 0..127 |  |
| 21 | 12 | Contr 12 | 0..127 |  |
| 22 | 13 | Contr 13 | 0..127 |  |
| 23 | 14 | Contr 14 | 0..127 |  |
| 24 | 15 | Contr 15 | 0..127 |  |
| 25 | 16 | Contr 16 | 0..127 |  |
| 26 | 17 | Osc1 Shape | 0..127 | oscShape |
| 27 | 18 | Osc1 Pulsewidth | 0..127 |  |
| 28 | 19 | Osc1 Wave Select | 0..63 | oscWave |
| 29 | 20 | Osc1 Semitone | 16..112 | signed |
| 30 | 21 | Osc1 Keyfollow | 0..127 | signedNorm |
| 31 | 22 | Osc2 Shape | 0..127 | oscShape |
| 32 | 23 | Osc2 Pulsewidth | 0..127 |  |
| 33 | 24 | Osc2 Wave Select | 0..63 | oscWave |
| 34 | 25 | Osc2 Semitone | 16..112 | signed |
| 35 | 26 | Osc2 Detune | 0..127 |  |
| 36 | 27 | Osc2 FM Amount | 0..127 | unipolarPercent |
| 37 | 28 | Osc2 Sync | 0..1 |  |
| 38 | 29 | Osc2 Filt Env Amt | 0..127 | biPolarPercent |
| 39 | 30 | FM Filt Env Amt | 0..127 | biPolarPercent |
| 40 | 31 | Osc2 Keyfollow | 0..127 | signedNorm |
| 41 | 32 | Bank Select | 0..8 | bank |
| 42 | 33 | Osc Balance | 0..127 | biPolarPercent |
| 43 | 34 | Suboscillator Volume | 0..127 |  |
| 44 | 35 | Suboscillator Shape | 0..1 | suboscShape |
| 45 | 36 | Osc Mainvolume | 0..127 | pan |
| 46 | 37 | Noise Volume | 0..127 | unsignedOff |
| 48 | 39 | Noise Color | 0..127 | signed |
| 49 | 40 | Cutoff | 0..127 |  |
| 50 | 41 | Cutoff2 | 0..127 |  |
| 51 | 42 | Filter1 Resonance | 0..127 |  |
| 52 | 43 | Filter2 Resonance | 0..127 |  |
| 53 | 44 | Filter1 Env Amt | 0..127 | unipolarPercent |
| 54 | 45 | Filter2 Env Amt | 0..127 | unipolarPercent |
| 55 | 46 | Filter1 Keyfollow | 0..127 | signed |
| 56 | 47 | Filter2 Keyfollow | 0..127 | signed |
| 57 | 48 | Filter Balance | 0..127 | pan |
| 58 | 49 | Saturation Curve | 0..14 | satCurve |
| 59 | 50 | Ringmodulator Volume | 0..127 |  |
| 60 | 51 | Filter1 Mode | 0..7 | filter1Mode |
| 61 | 52 | Filter2 Mode | 0..3 | filter2Mode |
| 62 | 53 | Filter Routing | 0..3 | filterRouting |
| 63 | 54 | Filter Env Attack | 0..127 |  |
| 64 | 55 | Filter Env Decay | 0..127 |  |
| 65 | 56 | Filter Env Sustain | 0..127 | unipolarPercent |
| 66 | 57 | Filter Env Sustain Time | 0..127 | envSustainTime |
| 67 | 58 | Filter Env Release | 0..127 |  |
| 68 | 59 | Amp Env Attack | 0..127 |  |
| 69 | 60 | Amp Env Decay | 0..127 |  |
| 70 | 61 | Amp Env Sustain | 0..127 | unipolarPercent |
| 71 | 62 | Amp Env Sustain Time | 0..127 | envSustainTime |
| 72 | 63 | Amp Env Release | 0..127 |  |
| 73 | 64 | Hold Pedal | 0..127 |  |
| 74 | 65 | Portamento Pedal | 0..127 |  |
| 75 | 66 | Sostenuto Pedal | 0..127 |  |
| 76 | 67 | Lfo1 Rate | 0..127 |  |
| 77 | 68 | Lfo1 Shape | 0..67 | lfoShape |
| 78 | 69 | Lfo1 Env Mode | 0..1 |  |
| 79 | 70 | Lfo1 Mode | 0..1 | lfoMode |
| 80 | 71 | Lfo1 Symmetry | 0..127 | signed |
| 81 | 72 | Lfo1 Keyfollow | 0..127 | unipolarPercentOff |
| 82 | 73 | Lfo1 Keytrigger | 0..127 | unsignedOff |
| 83 | 74 | Osc1 Lfo1 Amount | 0..127 | biPolarPercent |
| 84 | 75 | Osc2 Lfo1 Amount | 0..127 | biPolarPercent |
| 85 | 76 | PW Lfo1 Amount | 0..127 | biPolarPercent |
| 86 | 77 | Reso Lfo1 Amount | 0..127 | biPolarPercent |
| 87 | 78 | FiltGain Lfo1 Amount | 0..127 | biPolarPercent |
| 88 | 79 | Lfo2 Rate | 0..127 |  |
| 89 | 80 | Lfo2 Shape | 0..67 | lfoShape |
| 90 | 81 | Lfo2 Env Mode | 0..1 |  |
| 91 | 82 | Lfo2 Mode | 0..1 | lfoMode |
| 92 | 83 | Lfo2 Symmetry | 0..127 | signed |
| 93 | 84 | Lfo2 Keyfollow | 0..127 | unipolarPercentOff |
| 94 | 85 | Lfo2 Keytrigger | 0..127 | unsignedOff |
| 95 | 86 | Shape Lfo2 Amount | 0..127 | biPolarPercent |
| 96 | 87 | FM Lfo2 Amount | 0..127 | biPolarPercent |
| 97 | 88 | Cutoff1 Lfo2 Amount | 0..127 | biPolarPercent |
| 98 | 89 | Cutoff2 Lfo2 Amount | 0..127 | biPolarPercent |
| 99 | 90 | Pan Lfo2 Amount | 0..127 | biPolarPercent |
| 100 | 91 | Patch Volume | 0..127 |  |
| 101 | 92 | A_Undefined92 | 0..127 | unsignedZero |
| 102 | 93 | Transpose | 0..127 | signedMidOff |
| 103 | 94 | Key Mode | 0..5 | keyMode |
| 104 | 95 | A_Undefined95 | 0..127 | unsignedZero |
| 105 | 96 | A_Undefined96 | 0..127 | unsignedZero |
| 106 | 97 | A_Undefined97 | 0..127 | unsignedZero |
| 107 | 98 | A_Undefined98 | 0..127 | unsignedZero |
| 108 | 99 | A_Undefined99 | 0..127 | unsignedZero |
| 109 | 100 | A_Undefined100 | 0..127 | unsignedZero |
| 110 | 101 | A_Undefined101 | 0..127 | unsignedZero |
| 111 | 102 | A_Undefined102 | 0..127 | unsignedZero |
| 112 | 103 | Chorus/Type | 0..6 | chorusType |
| 113 | 104 | Chorus/Mix2 | 0..127 |  |
| 114 | 105 | Chorus Mix | 0..127 | unsignedOff |
| 115 | 106 | Chorus Rate | 0..127 |  |
| 116 | 107 | Chorus Depth | 0..127 | unipolarPercent |
| 117 | 108 | Chorus Delay | 0..127 |  |
| 118 | 109 | Chorus Feedback | 0..127 | biPolarPercent |
| 119 | 110 | Chorus Lfo Shape | 0..5 | lfoShape |
| 120 | 111 | Chorus/X Over | 0..127 | unsignedZero |
| 121 | 112 | Delay Mode | 0..22 | delayMode |
| 122 | 113 | Delay Send | 0..127 | send |
| 123 | 114 | Delay Time | 0..127 | delayTime |
| 124 | 115 | Delay Feedback | 0..127 | unipolarPercent |
| 125 | 116 | Dly Rate / Rev Decay | 0..127 |  |
| 126 | 117 | Dly Depth  | 0..127 | unipolarPercent |
| 127 | 118 | Reverb Damping | 0..127 | unipolarPercent |
| 128 | 119 | Delay Color | 0..127 | signed |
| 129 | 120 | A_Undefined120 | 0..127 | unsignedZero |
| 130 | 121 | A_Undefined121 | 0..127 | unsignedZero |
| 131 | 122 | Keyb Local | 0..1 |  |
| 132 | 123 | All Notes Off | 0..127 |  |
| 133 | 124 | A_Undefined124 | 0..127 | unsignedZero |
| 134 | 125 | A_Undefined125 | 0..127 | unsignedZero |
| 135 | 126 | A_Undefined126 | 0..127 | unsignedZero |
| 136 | 127 | A_Undefined127 | 0..127 | unsignedZero |
| 137 | 128 | B_Undefined0 | 0..127 | unsignedZero |
| 138 | 129 | B_Undefined1 | 0..127 | unsignedZero |
| 139 | 130 | Arp Pattern Selct | 0..63 | User1-64 |
| 140 | 131 | Arp Octave Range | 0..3 | MIDIChannels |
| 141 | 132 | Arp Hold Enable | 0..1 | OnOff |
| 142 | 133 | Arp Note Length | 0..127 | biPolarPercent |
| 143 | 134 | Arp Swing | 0..127 | arpSwing |
| 144 | 135 | Lfo3 Rate | 0..127 |  |
| 145 | 136 | Lfo3 Shape | 0..67 | lfoShape |
| 146 | 137 | Lfo3 Mode | 0..1 | lfoMode |
| 147 | 138 | Lfo3 Keyfollow | 0..127 | unipolarPercentOff |
| 148 | 139 | Lfo3 Destination | 0..6 | lfoDest |
| 149 | 140 | Osc Lfo3 Amount | 0..127 | unipolarPercent |
| 150 | 141 | Lfo3 Fade-In Time | 0..127 |  |
| 151 | 142 | B_Undefined14 | 0..127 | unsignedZero |
| 152 | 143 | Arp Mode | 0..7 | arpModes |
| 153 | 144 | Clock Tempo | 0..127 | bpm |
| 154 | 145 | Arp Clock | 0..17 | numArpClockdividers |
| 155 | 146 | Lfo1 Clock | 0..21 | numLFOClockdividers |
| 156 | 147 | Lfo2 Clock | 0..21 | numLFOClockdividers |
| 157 | 148 | Delay Clock | 0..16 | numDelayClockdividers |
| 158 | 149 | Lfo3 Clock | 0..21 | numLFOClockdividers |
| 159 | 150 | B_Undefined22 | 0..127 | unsignedZero |
| 160 | 151 | B_Undefined23 | 0..127 | unsignedZero |
| 161 | 152 | B_Undefined24 | 0..127 | unsignedZero |
| 162 | 153 | Control Smooth Mode | 0..20 | controlSmoothMode |
| 163 | 154 | Bender Range Up | 0..127 | signed |
| 164 | 155 | Bender Range Down | 0..127 | signed |
| 165 | 156 | Bender Scale | 0..1 | linExp |
| 166 | 157 | B_Undefined29 | 0..127 | unsignedZero |
| 167 | 158 | Filter1 Env Polarity | 0..1 | negPos |
| 168 | 159 | Filter2 Env Polarity | 0..1 | negPos |
| 169 | 160 | Filter2 Cutoff Link | 0..1 |  |
| 170 | 161 | Filter Keytrack Base | 0..127 | filterKeytrackBase |
| 171 | 162 | Osc FM Mode | 0..6 | oscFMMode |
| 172 | 163 | Osc Init Phase | 0..127 | unsignedOff |
| 173 | 164 | Punch Intensity | 0..127 | unipolarPercent |
| 174 | 165 | B_Undefined37 | 0..127 | unsignedZero |
| 175 | 166 | Input Follower Mode | 0..3 | inputFollowerMode |
| 176 | 167 | Vocoder Mode | 0..6 | vocoderMode |
| 177 | 168 | B_Undefined40 | 0..127 | unsignedZero |
| 178 | 169 | Osc3 Mode | 0..67 | osc3Mode |
| 179 | 170 | Osc3 Volume | 0..127 |  |
| 180 | 171 | Osc3 Semitone | 16..112 | signed |
| 181 | 172 | Osc3 Detune | 0..127 | nagativ |
| 182 | 173 | LowEQ Frequency | 0..127 | numEQLowFrequency |
| 183 | 174 | HighEQ Frequency | 0..127 | numEQHighFrequency |
| 184 | 175 | Osc1 Shape Velocity | 0..127 | biPolarPercent |
| 185 | 176 | Osc2 Shape Velocity | 0..127 | biPolarPercent |
| 186 | 177 | PulseWidth Velocity | 0..127 | biPolarPercent |
| 187 | 178 | Fm Amount Velocity | 0..127 | biPolarPercent |
| 188 | 179 | Soft Knob1 ShortName | 0..87 | softknobName |
| 189 | 180 | Soft Knob2 ShortName | 0..87 | softknobName |
| 190 | 181 | Soft Knob3 ShortName | 0..87 | softknobName |
| 191 | 182 | Flt1 EnvAmt Velocity | 0..127 | biPolarPercent |
| 192 | 183 | Flt2 EnvAmt Velocity | 0..127 | biPolarPercent |
| 193 | 184 | Resonance1 Velocity | 0..127 | biPolarPercent |
| 194 | 185 | Resonance2 Velocity | 0..127 | biPolarPercent |
| 195 | 186 | Second Output Balance | 0..127 | signed |
| 196 | 187 | B_Undefined59 | 0..127 | unsignedZero |
| 197 | 188 | Amp Velocity | 0..127 | biPolarPercent |
| 198 | 189 | Panorama Velocity | 0..127 | biPolarPercent |
| 199 | 190 | Soft Knob-1 Single | 0..127 | softknobDest |
| 200 | 191 | Soft Knob-2 Single | 0..127 | softknobDest |
| 201 | 192 | Assign1 Source | 0..39 | modmatrixSource |
| 202 | 193 | Assign1 Destination | 0..127 | modmatrixDest |
| 203 | 194 | Assign1 Amount | 0..127 | signedMidOff |
| 204 | 195 | Assign2 Source | 0..39 | modmatrixSource |
| 205 | 196 | Assign2 Destination1 | 0..127 | modmatrixDest |
| 206 | 197 | Assign2 Amount1 | 0..127 | signedMidOff |
| 207 | 198 | Assign2 Destination2 | 0..127 | modmatrixDest |
| 208 | 199 | Assign2 Amount2 | 0..127 | signedMidOff |
| 209 | 200 | Assign3 Source | 0..39 | modmatrixSource |
| 210 | 201 | Assign3 Destination1 | 0..127 | modmatrixDest |
| 211 | 202 | Assign3 Amount1 | 0..127 | signedMidOff |
| 212 | 203 | Assign3 Destination2 | 0..127 | modmatrixDest |
| 213 | 204 | Assign3 Amount2 | 0..127 | signed |
| 214 | 205 | Assign3 Destination3 | 0..127 | modmatrixDest |
| 215 | 206 | Assign3 Amount3 | 0..127 | signedMidOff |
| 216 | 207 | LFO1 Assign Dest | 0..127 | modmatrixDest |
| 217 | 208 | LFO1 Assign Amount | 0..127 | biPolarPercent |
| 218 | 209 | LFO2 Assign Dest | 0..127 | modmatrixDest |
| 219 | 210 | LFO2 Assign Amount | 0..127 | biPolarPercent |
| 220 | 211 | B_Undefined83 | 0..127 | unsignedZero |
| 221 | 212 | Phaser Mode | 0..5 | phaserMode |
| 222 | 213 | Phaser Mix | 0..127 | unsignedOff |
| 223 | 214 | Phaser Rate | 0..127 |  |
| 224 | 215 | Phaser Depth | 0..127 |  |
| 225 | 216 | Phaser Frequency | 0..127 |  |
| 226 | 217 | Phaser Feedback | 0..127 | signed |
| 227 | 218 | Phaser Spread | 0..127 |  |
| 228 | 219 | B_Undefined91 | 0..127 | unsignedZero |
| 229 | 220 | MidEQ Gain | 0..127 | NumEqInDB |
| 230 | 221 | MidEQ Frequency | 0..127 | numEQMidFrequency |
| 231 | 222 | MidEQ Q-Factor | 0..127 | NumEQQ-factor |
| 232 | 223 | LowEQ Gain | 0..127 | NumEqInDB |
| 233 | 224 | HighEQ Gain | 0..127 | NumEqInDB |
| 234 | 225 | Bass Intensity | 0..127 | unipolarPercentOff |
| 235 | 226 | Bass Tune | 0..127 |  |
| 236 | 227 | Input Ringmodulator | 0..127 | unsignedOff |
| 237 | 228 | Distortion Curve | 0..25 | NameDistortionModes |
| 238 | 229 | Distortion Intensity | 0..127 | unipolarPercent |
| 239 | 230 | B_Undefined102 | 0..127 | unsignedZero |
| 240 | 231 | Assign 4 Source | 0..39 | modmatrixSource |
| 241 | 232 | Assign 4 Destination | 0..127 | modmatrixDest |
| 242 | 233 | Assign 4 Amount | 0..127 | signedMidOff |
| 243 | 234 | Assign 5 Source | 0..39 | modmatrixSource |
| 244 | 235 | Assign 5 Destination | 0..127 | modmatrixDest |
| 245 | 236 | Assign 5 Amount | 0..127 | signedMidOff |
| 246 | 237 | Assign 6 Source | 0..39 | modmatrixSource |
| 247 | 238 | Assign 6 Destination | 0..127 | modmatrixDest |
| 248 | 239 | Assign 6 Amount | 0..127 | signedMidOff |
| 249 | 240 | SingleName0 | 0..127 | ascii |
| 250 | 241 | SingleName1 | 0..127 | ascii |
| 251 | 242 | SingleName2 | 0..127 | ascii |
| 252 | 243 | SingleName3 | 0..127 | ascii |
| 253 | 244 | SingleName4 | 0..127 | ascii |
| 254 | 245 | SingleName5 | 0..127 | ascii |
| 255 | 246 | SingleName6 | 0..127 | ascii |
| 256 | 247 | SingleName7 | 0..127 | ascii |
| 257 | 248 | SingleName8 | 0..127 | ascii |
| 258 | 249 | SingleName9 | 0..127 | ascii |
| 259 | 250 | Filter Select | 0..2 | filterSelect |
| 260 | 251 | Category1 | 0..22 | category |
| 261 | 252 | Category2 | 0..22 | category |
| 262 | 253 | B_Undefined125 | 0..127 | unsignedZero |
| 263 | 254 | B_Undefined126 | 0..127 | unsignedZero |
| 264 | 255 | Oscillators/Select | 0..2 |  |
| 266 | 257 | 6E_Undefined0 | 0..127 | unsignedZero |
| 267 | 258 | Reverb Mode | 0..3 | reverbMode |
| 268 | 259 | Reverb Send | 0..127 | send |
| 269 | 260 | Reverb Type | 0..3 | reverbType |
| 270 | 261 | Reverb Time | 0..127 |  |
| 271 | 262 | Reverb Damping | 0..127 | unipolarPercent |
| 272 | 263 | Reverb Color | 0..127 | signed |
| 273 | 264 | Reverb Predelay | 0..92 | numDelay500 |
| 274 | 265 | Reverb Clock | 0..16 | numDelayClockdividers |
| 275 | 266 | Reverb Feedback | 0..127 |  |
| 276 | 267 | Delay Type | 0..3 | delayType |
| 277 | 268 | 6E_Undefined11 | 0..127 | unsignedZero |
| 278 | 269 | Delay Tape Delay Ratio | 0..6 | delayRatio |
| 279 | 270 | Delay Tape Delay Left Clock | 0..5 | tapeDelayClock |
| 280 | 271 | Delay Tape Delay Right Clock | 0..5 | tapeDelayClock |
| 281 | 272 | 6E_Undefined15 | 0..127 | unsignedZero |
| 282 | 273 | 6E_Undefined16 | 0..127 | unsignedZero |
| 283 | 274 | Delay Tape Delay Bandwidth | 0..127 |  |
| 284 | 275 | 6E_Undefined18 | 0..127 | unsignedZero |
| 285 | 276 | Filter Bank/Type | 0..11 | filterBankType |
| 286 | 277 | Filter Bank/Mix | 0..127 | unipolarPercentOff |
| 287 | 278 | Filter Bank/Comb Frequency | 0..96 | nameCombFilter |
| 288 | 279 | Filter Bank/Stereo Phase | 0..127 | -180Degree+180Degree |
| 289 | 280 | Filter Bank/Shape L | 0..127 | biPolarPercent |
| 290 | 281 | Filter Bank/Shape R | 0..127 | biPolarPercent |
| 291 | 282 | Filter Bank/Resonance | 0..127 | unipolarPercent |
| 292 | 283 | Character Type | 0..8 | characters |
| 293 | 284 | 6E_Undefined27 | 0..127 | unsignedZero |
| 294 | 285 | Soft Knobs/Destination 3 | 0..127 | softknobDest |
| 295 | 286 | 6E_Undefined29 | 0..127 | unsignedZero |
| 296 | 287 | Osc1 Mode | 0..7 | nameOscillator12Mode |
| 297 | 288 | 6E_Undefined31 | 0..127 | unsignedZero |
| 298 | 289 | 6E_Undefined32 | 0..127 | unsignedZero |
| 299 | 290 | 6E_Undefined33 | 0..127 | unsignedZero |
| 300 | 291 | 6E_Undefined34 | 0..127 | unsignedZero |
| 301 | 292 | Osc2 Mode | 0..7 | nameOscillator12Mode |
| 302 | 293 | 6E_Undefined36 | 0..127 | unsignedZero |
| 303 | 294 | Osc1 Wavetable/Sync | 0..127 |  |
| 304 | 295 | 6E_Undefined38 | 0..127 | unsignedZero |
| 305 | 296 | 6E_Undefined39 | 0..127 | unsignedZero |
| 306 | 297 | 6E_Undefined40 | 0..127 | unsignedZero |
| 307 | 298 | 6E_Undefined41 | 0..127 | unsignedZero |
| 308 | 299 | Osc1 Wavetable/FormantShift | 0..127 | signed |
| 309 | 300 | Osc1 Wavetable/Internal Detune | 0..127 |  |
| 310 | 301 | Osc1 Wavetable/Interpolation | 0..127 |  |
| 311 | 302 | 6E_Undefined45 | 0..127 | unsignedZero |
| 312 | 303 | 6E_Undefined46 | 0..127 | unsignedZero |
| 313 | 304 | 6E_Undefined47 | 0..127 | unsignedZero |
| 314 | 305 | 6E_Undefined48 | 0..127 | unsignedZero |
| 315 | 306 | 6E_Undefined49 | 0..127 | unsignedZero |
| 316 | 307 | 6E_Undefined50 | 0..127 | unsignedZero |
| 317 | 308 | 6E_Undefined51 | 0..127 | unsignedZero |
| 318 | 309 | 6E_Undefined52 | 0..127 | unsignedZero |
| 319 | 310 | 6E_Undefined53 | 0..127 | unsignedZero |
| 320 | 311 | 6E_Undefined54 | 0..127 | unsignedZero |
| 321 | 312 | 6E_Undefined55 | 0..127 | unsignedZero |
| 322 | 313 | 6E_Undefined56 | 0..127 | unsignedZero |
| 323 | 314 | Osc2 Wavetable/Sync | 0..127 |  |
| 324 | 315 | 6E_Undefined58 | 0..127 | unsignedZero |
| 325 | 316 | 6E_Undefined59 | 0..127 | unsignedZero |
| 326 | 317 | 6E_Undefined60 | 0..127 | unsignedZero |
| 327 | 318 | 6E_Undefined61 | 0..127 | unsignedZero |
| 328 | 319 | Osc2 Wavetable/FormantShift | 0..127 | signed |
| 329 | 320 | Osc2 Wavetable/Internal Detune | 0..127 |  |
| 330 | 321 | Osc2 Wavetable/Interpolation | 0..127 |  |
| 331 | 322 | 6E_Undefined65 | 0..127 | unsignedZero |
| 332 | 323 | 6E_Undefined66 | 0..127 | unsignedZero |
| 333 | 324 | 6E_Undefined67 | 0..127 | unsignedZero |
| 334 | 325 | 6E_Undefined68 | 0..127 | unsignedZero |
| 335 | 326 | 6E_Undefined69 | 0..127 | unsignedZero |
| 336 | 327 | Patch Distortion/Treble Booster | 0..127 | unipolarPercent |
| 337 | 328 | Patch Distortion/High Cut | 0..127 | unipolarPercent |
| 338 | 329 | Patch Distortion/Mix | 0..127 | unipolarPercent |
| 339 | 330 | Patch Distortion/Quality | 0..127 | unipolarPercent |
| 340 | 331 | Patch Distortion/Tone127 | 0..127 | biPolarPercent |
| 341 | 332 | 6E_Undefined75 | 0..127 | unsignedZero |
| 342 | 333 | 6E_Undefined76 | 0..127 | unsignedZero |
| 343 | 334 | 6E_Undefined77 | 0..127 | unsignedZero |
| 344 | 335 | 6E_Undefined78 | 0..127 | unsignedZero |
| 345 | 336 | 6E_Undefined79 | 0..127 | unsignedZero |
| 346 | 337 | Envelope 3/Attack | 0..127 |  |
| 347 | 338 | Envelope 3/Decay | 0..127 |  |
| 348 | 339 | Envelope 3/Sustain | 0..127 | unipolarPercent |
| 349 | 340 | Envelope 3/Sustain Time | 0..127 | envSustainTime |
| 350 | 341 | Envelope 3/Release | 0..127 |  |
| 351 | 342 | Envelope 4/Attack | 0..127 |  |
| 352 | 343 | Envelope 4/Decay | 0..127 |  |
| 353 | 344 | Envelope 4/Sustain | 0..127 | unipolarPercent |
| 354 | 345 | Envelope 4/Sustain Time | 0..127 | envSustainTime |
| 355 | 346 | Envelope 4/Release | 0..127 |  |
| 356 | 347 | Assign 1 Destination 2 | 0..127 | modmatrixDest |
| 357 | 348 | Assign 1 Amount 2 | 0..127 | signedMidOff |
| 358 | 349 | Assign 1 Destination 3 | 0..127 | modmatrixDest |
| 359 | 350 | Assign 1 Amount 3 | 0..127 | signedMidOff |
| 360 | 351 | Assign 2 Destination 3 | 0..127 | modmatrixDest |
| 361 | 352 | Assign 2 Amount 3 | 0..127 | signedMidOff |
| 362 | 353 | Assign 4 Destination 2 | 0..127 | modmatrixDest |
| 363 | 354 | Assign 4 Amount 2 | 0..127 | signedMidOff |
| 364 | 355 | Assign 4 Destination 3 | 0..127 | modmatrixDest |
| 365 | 356 | Assign 4 Amount 3 | 0..127 | signedMidOff |
| 366 | 357 | Assign 5 Destination 2 | 0..127 | modmatrixDest |
| 367 | 358 | Assign 5 Amount 2 | 0..127 | signedMidOff |
| 368 | 359 | Assign 5 Destination 3 | 0..127 | modmatrixDest |
| 369 | 360 | Assign 5 Amount 3 | 0..127 | signedMidOff |
| 370 | 361 | Assign 6 Destination 2 | 0..127 | modmatrixDest |
| 371 | 362 | Assign 6 Amount 2 | 0..127 | signedMidOff |
| 372 | 363 | Assign 6 Destination 3 | 0..127 | modmatrixDest |
| 373 | 364 | Assign 6 Amount 3 | 0..127 | signedMidOff |
| 374 | 365 | 6E_Undefined108 | 0..127 | unsignedZero |
| 375 | 366 | 6E_Undefined109 | 0..127 | unsignedZero |
| 376 | 367 | LFO 1/BackupShape | 0..67 | lfoShape |
| 377 | 368 | LFO 2/BackupShape | 0..67 | lfoShape |
| 378 | 369 | LFO 3/BackupShape | 0..67 | lfoShape |
| 379 | 370 | 6E_Undefined113 | 0..127 | unsignedZero |
| 380 | 371 | 6E_Undefined114 | 0..127 | unsignedZero |
| 381 | 372 | Assigns/Slot Select | 0..17 |  |
| 382 | 373 | LFOs/Select | 0..16 |  |
| 383 | 374 | FX Upper/Select | 0..16 |  |
| 384 | 375 | FX Lower/Select | 0..16 |  |
| 385 | 376 | Oscillators/BackupKeyMode | 1..4 | keyMode |
| 386 | 377 | 6E_Undefined120 | 0..127 | unsignedZero |
| 387 | 378 | 6E_Undefined121 | 0..127 | unsignedZero |
| 388 | 379 | Oscillators/BackupKeyMode | 1..4 | keyMode |
| 389 | 380 | Arpeggiator/BackupMode | 1..7 |  |
| 390 | 381 | Osc 3/BackupMode | 1..66 | osc3Mode |
| 391 | 382 | 6E_Undefined125 | 0..127 | unsignedZero |
| 392 | 383 | 6E_Undefined126 | 0..127 | unsignedZero |
| 393 | 384 | Arpeggiator/UserPatternLength | 0..31 | MIDIChannels |
| 394 | 385 | Step 1 Length | 0..127 |  |
| 395 | 386 | Step 1 Velocity | 0..127 |  |
| 396 | 387 | Step 1 Bitfield | 0..1 |  |
| 397 | 388 | Step 2 Length | 0..127 |  |
| 398 | 389 | Step 2 Velocity | 0..127 |  |
| 399 | 390 | Step 2 Bitfield | 0..1 |  |
| 400 | 391 | Step 3 Length | 0..127 |  |
| 401 | 392 | Step 3 Velocity | 0..127 |  |
| 402 | 393 | Step 3 Bitfield | 0..1 |  |
| 403 | 394 | Step 4 Length | 0..127 |  |
| 404 | 395 | Step 4 Velocity | 0..127 |  |
| 405 | 396 | Step 4 Bitfield | 0..1 |  |
| 406 | 397 | Step 5 Length | 0..127 |  |
| 407 | 398 | Step 5 Velocity | 0..127 |  |
| 408 | 399 | Step 5 Bitfield | 0..1 |  |
| 409 | 400 | Step 6 Length | 0..127 |  |
| 410 | 401 | Step 6 Velocity | 0..127 |  |
| 411 | 402 | Step 6 Bitfield | 0..1 |  |
| 412 | 403 | Step 7 Length | 0..127 |  |
| 413 | 404 | Step 7 Velocity | 0..127 |  |
| 414 | 405 | Step 7 Bitfield | 0..1 |  |
| 415 | 406 | Step 8 Length | 0..127 |  |
| 416 | 407 | Step 8 Velocity | 0..127 |  |
| 417 | 408 | Step 8 Bitfield | 0..1 |  |
| 418 | 409 | Step 9 Length | 0..127 |  |
| 419 | 410 | Step 9 Velocity | 0..127 |  |
| 420 | 411 | Step 9 Bitfield | 0..1 |  |
| 421 | 412 | Step 10 Length | 0..127 |  |
| 422 | 413 | Step 10 Velocity | 0..127 |  |
| 423 | 414 | Step 10 Bitfield | 0..1 |  |
| 424 | 415 | Step 11 Length | 0..127 |  |
| 425 | 416 | Step 11 Velocity | 0..127 |  |
| 426 | 417 | Step 11 Bitfield | 0..1 |  |
| 427 | 418 | Step 12 Length | 0..127 |  |
| 428 | 419 | Step 12 Velocity | 0..127 |  |
| 429 | 420 | Step 12 Bitfield | 0..1 |  |
| 430 | 421 | Step 13 Length | 0..127 |  |
| 431 | 422 | Step 13 Velocity | 0..127 |  |
| 432 | 423 | Step 13 Bitfield | 0..1 |  |
| 433 | 424 | Step 14 Length | 0..127 |  |
| 434 | 425 | Step 14 Velocity | 0..127 |  |
| 435 | 426 | Step 14 Bitfield | 0..1 |  |
| 436 | 427 | Step 15 Length | 0..127 |  |
| 437 | 428 | Step 15 Velocity | 0..127 |  |
| 438 | 429 | Step 15 Bitfield | 0..1 |  |
| 439 | 430 | Step 16 Length | 0..127 |  |
| 440 | 431 | Step 16 Velocity | 0..127 |  |
| 441 | 432 | Step 16 Bitfield | 0..1 |  |
| 442 | 433 | Step 17 Length | 0..127 |  |
| 443 | 434 | Step 17 Velocity | 0..127 |  |
| 444 | 435 | Step 17 Bitfield | 0..1 |  |
| 445 | 436 | Step 18 Length | 0..127 |  |
| 446 | 437 | Step 18 Velocity | 0..127 |  |
| 447 | 438 | Step 18 Bitfield | 0..1 |  |
| 448 | 439 | Step 19 Length | 0..127 |  |
| 449 | 440 | Step 19 Velocity | 0..127 |  |
| 450 | 441 | Step 19 Bitfield | 0..1 |  |
| 451 | 442 | Step 20 Length | 0..127 |  |
| 452 | 443 | Step 20 Velocity | 0..127 |  |
| 453 | 444 | Step 20 Bitfield | 0..1 |  |
| 454 | 445 | Step 21 Length | 0..127 |  |
| 455 | 446 | Step 21 Velocity | 0..127 |  |
| 456 | 447 | Step 21 Bitfield | 0..1 |  |
| 457 | 448 | Step 22 Length | 0..127 |  |
| 458 | 449 | Step 22 Velocity | 0..127 |  |
| 459 | 450 | Step 22 Bitfield | 0..1 |  |
| 460 | 451 | Step 23 Length | 0..127 |  |
| 461 | 452 | Step 23 Velocity | 0..127 |  |
| 462 | 453 | Step 23 Bitfield | 0..1 |  |
| 463 | 454 | Step 24 Length | 0..127 |  |
| 464 | 455 | Step 24 Velocity | 0..127 |  |
| 465 | 456 | Step 24 Bitfield | 0..1 |  |
| 466 | 457 | Step 25 Length | 0..127 |  |
| 467 | 458 | Step 25 Velocity | 0..127 |  |
| 468 | 459 | Step 25 Bitfield | 0..1 |  |
| 469 | 460 | Step 26 Length | 0..127 |  |
| 470 | 461 | Step 26 Velocity | 0..127 |  |
| 471 | 462 | Step 26 Bitfield | 0..1 |  |
| 472 | 463 | Step 27 Length | 0..127 |  |
| 473 | 464 | Step 27 Velocity | 0..127 |  |
| 474 | 465 | Step 27 Bitfield | 0..1 |  |
| 475 | 466 | Step 28 Length | 0..127 |  |
| 476 | 467 | Step 28 Velocity | 0..127 |  |
| 477 | 468 | Step 28 Bitfield | 0..1 |  |
| 478 | 469 | Step 29 Length | 0..127 |  |
| 479 | 470 | Step 29 Velocity | 0..127 |  |
| 480 | 471 | Step 29 Bitfield | 0..1 |  |
| 481 | 472 | Step 30 Length | 0..127 |  |
| 482 | 473 | Step 30 Velocity | 0..127 |  |
| 483 | 474 | Step 30 Bitfield | 0..1 |  |
| 484 | 475 | Step 31 Length | 0..127 |  |
| 485 | 476 | Step 31 Velocity | 0..127 |  |
| 486 | 477 | Step 31 Bitfield | 0..1 |  |
| 487 | 478 | Step 32 Length | 0..127 |  |
| 488 | 479 | Step 32 Velocity | 0..127 |  |
| 489 | 480 | Step 32 Bitfield | 0..1 |  |
| 490 | 481 | 6F_Undefined96 | 0..127 | unsignedZero |
| 491 | 482 | 6F_Undefined97 | 0..127 | unsignedZero |
| 492 | 483 | 6F_Undefined98 | 0..127 | unsignedZero |
| 493 | 484 | 6F_Undefined99 | 0..127 | unsignedZero |
| 494 | 485 | 6F_Undefined100 | 0..127 | unsignedZero |
| 495 | 486 | 6F_Undefined101 | 0..127 | unsignedZero |
| 496 | 487 | 6F_Undefined102 | 0..127 | unsignedZero |
| 497 | 488 | 6F_Undefined103 | 0..127 | unsignedZero |
| 498 | 489 | 6F_Undefined104 | 0..127 | unsignedZero |
| 499 | 490 | 6F_Undefined105 | 0..127 | unsignedZero |
| 500 | 491 | 6F_Undefined106 | 0..127 | unsignedZero |
| 501 | 492 | 6F_Undefined107 | 0..127 | unsignedZero |
| 502 | 493 | 6F_Undefined108 | 0..127 | unsignedZero |
| 503 | 494 | 6F_Undefined109 | 0..127 | unsignedZero |
| 504 | 495 | 6F_Undefined110 | 0..127 | unsignedZero |
| 505 | 496 | 6F_Undefined111 | 0..127 | unsignedZero |
| 506 | 497 | 6F_Undefined112 | 0..127 | unsignedZero |
| 507 | 498 | 6F_Undefined113 | 0..127 | unsignedZero |
| 508 | 499 | 6F_Undefined114 | 0..127 | unsignedZero |
| 509 | 500 | 6F_Undefined115 | 0..127 | unsignedZero |
| 510 | 501 | 6F_Undefined116 | 0..127 | unsignedZero |
| 511 | 502 | 6F_Undefined117 | 0..127 | unsignedZero |
| 512 | 503 | 6F_Undefined118 | 0..127 | unsignedZero |
| 513 | 504 | 6F_Undefined119 | 0..127 | unsignedZero |
| 514 | 505 | Unison Mode | 0..7 | unisonMode |
| 515 | 506 | Unison Detune | 0..127 |  |
| 516 | 507 | Unison Pan Spread | 0..127 | unipolarPercent |
| 517 | 508 | Unison Lfo Phase | 0..127 | signed |
| 518 | 509 | Input Mode | 0..2 | nameInputMode |
| 519 | 510 | Input Select | 0..2 | nameInputSelectLeftRight |
| 520 | 511 | Atomizer | 0..16 | 0-16OnOff |
| 521 | 512 | 6F_Undefined127 | 0..127 | unsignedZero |

## Classic dump (267 bytes) — packet `singledump_C`

| msg | data | parameter | range | value type |
|----:|-----:|-----------|-------|------------|
| 9 | 0 | Version | 0..12 | version |
| 10 | 1 | Modulation Wheel | 0..127 |  |
| 11 | 2 | Breath Controller | 0..127 |  |
| 12 | 3 | Contr 3 | 0..127 |  |
| 13 | 4 | Foot Controller | 0..127 |  |
| 14 | 5 | Portamento Time | 0..127 | unsignedOff |
| 15 | 6 | Data Slider | 0..127 |  |
| 16 | 7 | Channel Volume | 0..127 |  |
| 17 | 8 | Balance | 0..127 |  |
| 18 | 9 | Contr 9 | 0..127 |  |
| 19 | 10 | Panorama | 0..127 | panPercent |
| 20 | 11 | Expression | 0..127 |  |
| 21 | 12 | Contr 12 | 0..127 |  |
| 22 | 13 | Contr 13 | 0..127 |  |
| 23 | 14 | Contr 14 | 0..127 |  |
| 24 | 15 | Contr 15 | 0..127 |  |
| 25 | 16 | Contr 16 | 0..127 |  |
| 26 | 17 | Osc1 Shape | 0..127 | oscShape |
| 27 | 18 | Osc1 Pulsewidth | 0..127 |  |
| 28 | 19 | Osc1 Wave Select | 0..63 | oscWave |
| 29 | 20 | Osc1 Semitone | 16..112 | signed |
| 30 | 21 | Osc1 Keyfollow | 0..127 | signedNorm |
| 31 | 22 | Osc2 Shape | 0..127 | oscShape |
| 32 | 23 | Osc2 Pulsewidth | 0..127 |  |
| 33 | 24 | Osc2 Wave Select | 0..63 | oscWave |
| 34 | 25 | Osc2 Semitone | 16..112 | signed |
| 35 | 26 | Osc2 Detune | 0..127 |  |
| 36 | 27 | Osc2 FM Amount | 0..127 | unipolarPercent |
| 37 | 28 | Osc2 Sync | 0..1 |  |
| 38 | 29 | Osc2 Filt Env Amt | 0..127 | biPolarPercent |
| 39 | 30 | FM Filt Env Amt | 0..127 | biPolarPercent |
| 40 | 31 | Osc2 Keyfollow | 0..127 | signedNorm |
| 41 | 32 | Bank Select | 0..8 | bank |
| 42 | 33 | Osc Balance | 0..127 | biPolarPercent |
| 43 | 34 | Suboscillator Volume | 0..127 |  |
| 44 | 35 | Suboscillator Shape | 0..1 | suboscShape |
| 45 | 36 | Osc Mainvolume | 0..127 | pan |
| 46 | 37 | Noise Volume | 0..127 | unsignedOff |
| 47 | 38 | Ringmodulator Volume | 0..127 |  |
| 48 | 39 | Noise Color | 0..127 | signed |
| 49 | 40 | Cutoff | 0..127 |  |
| 50 | 41 | Cutoff2 | 0..127 |  |
| 51 | 42 | Filter1 Resonance | 0..127 |  |
| 52 | 43 | Filter2 Resonance | 0..127 |  |
| 53 | 44 | Filter1 Env Amt | 0..127 | unipolarPercent |
| 54 | 45 | Filter2 Env Amt | 0..127 | unipolarPercent |
| 55 | 46 | Filter1 Keyfollow | 0..127 | signed |
| 56 | 47 | Filter2 Keyfollow | 0..127 | signed |
| 57 | 48 | Filter Balance | 0..127 | pan |
| 58 | 49 | Saturation Curve | 0..14 | satCurve |
| 60 | 51 | Filter1 Mode | 0..7 | filter1Mode |
| 61 | 52 | Filter2 Mode | 0..3 | filter2Mode |
| 62 | 53 | Filter Routing | 0..3 | filterRouting |
| 63 | 54 | Filter Env Attack | 0..127 |  |
| 64 | 55 | Filter Env Decay | 0..127 |  |
| 65 | 56 | Filter Env Sustain | 0..127 | unipolarPercent |
| 66 | 57 | Filter Env Sustain Time | 0..127 | envSustainTime |
| 67 | 58 | Filter Env Release | 0..127 |  |
| 68 | 59 | Amp Env Attack | 0..127 |  |
| 69 | 60 | Amp Env Decay | 0..127 |  |
| 70 | 61 | Amp Env Sustain | 0..127 | unipolarPercent |
| 71 | 62 | Amp Env Sustain Time | 0..127 | envSustainTime |
| 72 | 63 | Amp Env Release | 0..127 |  |
| 73 | 64 | Hold Pedal | 0..127 |  |
| 74 | 65 | Portamento Pedal | 0..127 |  |
| 75 | 66 | Sostenuto Pedal | 0..127 |  |
| 76 | 67 | Lfo1 Rate | 0..127 |  |
| 77 | 68 | Lfo1 Shape | 0..67 | lfoShape |
| 78 | 69 | Lfo1 Env Mode | 0..1 |  |
| 79 | 70 | Lfo1 Mode | 0..1 | lfoMode |
| 80 | 71 | Lfo1 Symmetry | 0..127 | signed |
| 81 | 72 | Lfo1 Keyfollow | 0..127 | unipolarPercentOff |
| 82 | 73 | Lfo1 Keytrigger | 0..127 | unsignedOff |
| 83 | 74 | Osc1 Lfo1 Amount | 0..127 | biPolarPercent |
| 84 | 75 | Osc2 Lfo1 Amount | 0..127 | biPolarPercent |
| 85 | 76 | PW Lfo1 Amount | 0..127 | biPolarPercent |
| 86 | 77 | Reso Lfo1 Amount | 0..127 | biPolarPercent |
| 87 | 78 | FiltGain Lfo1 Amount | 0..127 | biPolarPercent |
| 88 | 79 | Lfo2 Rate | 0..127 |  |
| 89 | 80 | Lfo2 Shape | 0..67 | lfoShape |
| 90 | 81 | Lfo2 Env Mode | 0..1 |  |
| 91 | 82 | Lfo2 Mode | 0..1 | lfoMode |
| 92 | 83 | Lfo2 Symmetry | 0..127 | signed |
| 93 | 84 | Lfo2 Keyfollow | 0..127 | unipolarPercentOff |
| 94 | 85 | Lfo2 Keytrigger | 0..127 | unsignedOff |
| 95 | 86 | Shape Lfo2 Amount | 0..127 | biPolarPercent |
| 96 | 87 | FM Lfo2 Amount | 0..127 | biPolarPercent |
| 97 | 88 | Cutoff1 Lfo2 Amount | 0..127 | biPolarPercent |
| 98 | 89 | Cutoff2 Lfo2 Amount | 0..127 | biPolarPercent |
| 99 | 90 | Pan Lfo2 Amount | 0..127 | biPolarPercent |
| 100 | 91 | Patch Volume | 0..127 |  |
| 101 | 92 | A_Undefined92 | 0..127 | unsignedZero |
| 102 | 93 | Transpose | 0..127 | signedMidOff |
| 103 | 94 | Key Mode | 0..5 | keyMode |
| 104 | 95 | A_Undefined95 | 0..127 | unsignedZero |
| 105 | 96 | A_Undefined96 | 0..127 | unsignedZero |
| 106 | 97 | Unison Mode | 0..7 | unisonMode |
| 107 | 98 | Unison Detune | 0..127 |  |
| 108 | 99 | Unison Pan Spread | 0..127 | unipolarPercent |
| 109 | 100 | Unison Lfo Phase | 0..127 | signed |
| 110 | 101 | Input Mode | 0..2 | nameInputMode |
| 111 | 102 | Input Select | 0..2 | nameInputSelectLeftRight |
| 114 | 105 | Chorus Mix | 0..127 | unsignedOff |
| 115 | 106 | Chorus Rate | 0..127 |  |
| 116 | 107 | Chorus Depth | 0..127 | unipolarPercent |
| 117 | 108 | Chorus Delay | 0..127 |  |
| 118 | 109 | Chorus Feedback | 0..127 | biPolarPercent |
| 119 | 110 | Chorus Lfo Shape | 0..5 | lfoShape |
| 121 | 112 | Reverb Mode | 0..3 | reverbMode |
| 122 | 113 | Reverb Send | 0..127 | send |
| 123 | 114 | Delay Time | 0..127 | delayTime |
| 124 | 115 | Delay Feedback | 0..127 | unipolarPercent |
| 125 | 116 | Dly Rate / Rev Decay | 0..127 |  |
| 126 | 117 | Dly Depth  | 0..127 | unipolarPercent |
| 127 | 118 | Reverb Damping | 0..127 | unipolarPercent |
| 128 | 119 | Delay Color | 0..127 | signed |
| 129 | 120 | A_Undefined120 | 0..127 | unsignedZero |
| 130 | 121 | A_Undefined121 | 0..127 | unsignedZero |
| 131 | 122 | Keyb Local | 0..1 |  |
| 132 | 123 | All Notes Off | 0..127 |  |
| 133 | 124 | A_Undefined124 | 0..127 | unsignedZero |
| 134 | 125 | A_Undefined125 | 0..127 | unsignedZero |
| 135 | 126 | A_Undefined126 | 0..127 | unsignedZero |
| 136 | 127 | A_Undefined127 | 0..127 | unsignedZero |
| 137 | 128 | B_Undefined0 | 0..127 | unsignedZero |
| 138 | 129 | Arp Mode | 0..7 | arpModes |
| 139 | 130 | Arp Pattern Selct | 0..63 | User1-64 |
| 140 | 131 | Arp Octave Range | 0..3 | MIDIChannels |
| 141 | 132 | Arp Hold Enable | 0..1 | OnOff |
| 142 | 133 | Arp Note Length | 0..127 | biPolarPercent |
| 143 | 134 | Arp Swing | 0..127 | arpSwing |
| 144 | 135 | Lfo3 Rate | 0..127 |  |
| 145 | 136 | Lfo3 Shape | 0..67 | lfoShape |
| 146 | 137 | Lfo3 Mode | 0..1 | lfoMode |
| 147 | 138 | Lfo3 Keyfollow | 0..127 | unipolarPercentOff |
| 148 | 139 | Lfo3 Destination | 0..6 | lfoDest |
| 149 | 140 | Osc Lfo3 Amount | 0..127 | unipolarPercent |
| 150 | 141 | Lfo3 Fade-In Time | 0..127 |  |
| 151 | 142 | B_Undefined14 | 0..127 | unsignedZero |
| 153 | 144 | Clock Tempo | 0..127 | bpm |
| 154 | 145 | Arp Clock | 0..17 | numArpClockdividers |
| 155 | 146 | Lfo1 Clock | 0..21 | numLFOClockdividers |
| 156 | 147 | Lfo2 Clock | 0..21 | numLFOClockdividers |
| 157 | 148 | Delay Clock | 0..16 | numDelayClockdividers |
| 158 | 149 | Lfo3 Clock | 0..21 | numLFOClockdividers |
| 159 | 150 | B_Undefined22 | 0..127 | unsignedZero |
| 160 | 151 | B_Undefined23 | 0..127 | unsignedZero |
| 161 | 152 | B_Undefined24 | 0..127 | unsignedZero |
| 162 | 153 | Control Smooth Mode | 0..20 | controlSmoothMode |
| 163 | 154 | Bender Range Up | 0..127 | signed |
| 164 | 155 | Bender Range Down | 0..127 | signed |
| 165 | 156 | Bender Scale | 0..1 | linExp |
| 166 | 157 | B_Undefined29 | 0..127 | unsignedZero |
| 167 | 158 | Filter1 Env Polarity | 0..1 | negPos |
| 168 | 159 | Filter2 Env Polarity | 0..1 | negPos |
| 169 | 160 | Filter2 Cutoff Link | 0..1 |  |
| 170 | 161 | Filter Keytrack Base | 0..127 | filterKeytrackBase |
| 171 | 162 | Osc FM Mode | 0..6 | oscFMMode |
| 172 | 163 | Osc Init Phase | 0..127 | unsignedOff |
| 173 | 164 | Punch Intensity | 0..127 | unipolarPercent |
| 174 | 165 | B_Undefined37 | 0..127 | unsignedZero |
| 175 | 166 | Input Follower Mode | 0..3 | inputFollowerMode |
| 176 | 167 | Vocoder Mode | 0..6 | vocoderMode |
| 177 | 168 | B_Undefined40 | 0..127 | unsignedZero |
| 178 | 169 | Osc3 Mode | 0..67 | osc3Mode |
| 179 | 170 | Osc3 Volume | 0..127 |  |
| 180 | 171 | Osc3 Semitone | 16..112 | signed |
| 181 | 172 | Osc3 Detune | 0..127 | nagativ |
| 182 | 173 | LowEQ Frequency | 0..127 | numEQLowFrequency |
| 183 | 174 | HighEQ Frequency | 0..127 | numEQHighFrequency |
| 184 | 175 | Osc1 Shape Velocity | 0..127 | biPolarPercent |
| 185 | 176 | Osc2 Shape Velocity | 0..127 | biPolarPercent |
| 186 | 177 | PulseWidth Velocity | 0..127 | biPolarPercent |
| 187 | 178 | Fm Amount Velocity | 0..127 | biPolarPercent |
| 188 | 179 | Soft Knob1 ShortName | 0..87 | softknobName |
| 189 | 180 | Soft Knob2 ShortName | 0..87 | softknobName |
| 191 | 182 | Flt1 EnvAmt Velocity | 0..127 | biPolarPercent |
| 192 | 183 | Flt2 EnvAmt Velocity | 0..127 | biPolarPercent |
| 193 | 184 | Resonance1 Velocity | 0..127 | biPolarPercent |
| 194 | 185 | Resonance2 Velocity | 0..127 | biPolarPercent |
| 195 | 186 | Second Output Balance | 0..127 | signed |
| 196 | 187 | B_Undefined59 | 0..127 | unsignedZero |
| 197 | 188 | Amp Velocity | 0..127 | biPolarPercent |
| 198 | 189 | Panorama Velocity | 0..127 | biPolarPercent |
| 199 | 190 | Soft Knob-1 Single | 0..127 | softknobDest |
| 200 | 191 | Soft Knob-2 Single | 0..127 | softknobDest |
| 201 | 192 | Assign1 Source | 0..39 | modmatrixSource |
| 202 | 193 | Assign1 Destination | 0..127 | modmatrixDest |
| 203 | 194 | Assign1 Amount | 0..127 | signedMidOff |
| 204 | 195 | Assign2 Source | 0..39 | modmatrixSource |
| 205 | 196 | Assign2 Destination1 | 0..127 | modmatrixDest |
| 206 | 197 | Assign2 Amount1 | 0..127 | signedMidOff |
| 207 | 198 | Assign2 Destination2 | 0..127 | modmatrixDest |
| 208 | 199 | Assign2 Amount2 | 0..127 | signedMidOff |
| 209 | 200 | Assign3 Source | 0..39 | modmatrixSource |
| 210 | 201 | Assign3 Destination1 | 0..127 | modmatrixDest |
| 211 | 202 | Assign3 Amount1 | 0..127 | signedMidOff |
| 212 | 203 | Assign3 Destination2 | 0..127 | modmatrixDest |
| 213 | 204 | Assign3 Amount2 | 0..127 | signed |
| 214 | 205 | Assign3 Destination3 | 0..127 | modmatrixDest |
| 215 | 206 | Assign3 Amount3 | 0..127 | signedMidOff |
| 216 | 207 | LFO1 Assign Dest | 0..127 | modmatrixDest |
| 217 | 208 | LFO1 Assign Amount | 0..127 | biPolarPercent |
| 218 | 209 | LFO2 Assign Dest | 0..127 | modmatrixDest |
| 219 | 210 | LFO2 Assign Amount | 0..127 | biPolarPercent |
| 220 | 211 | B_Undefined83 | 0..127 | unsignedZero |
| 221 | 212 | Phaser Mode | 0..5 | phaserMode |
| 222 | 213 | Phaser Mix | 0..127 | unsignedOff |
| 223 | 214 | Phaser Rate | 0..127 |  |
| 224 | 215 | Phaser Depth | 0..127 |  |
| 225 | 216 | Phaser Frequency | 0..127 |  |
| 226 | 217 | Phaser Feedback | 0..127 | signed |
| 227 | 218 | Phaser Spread | 0..127 |  |
| 228 | 219 | B_Undefined91 | 0..127 | unsignedZero |
| 229 | 220 | MidEQ Gain | 0..127 | NumEqInDB |
| 230 | 221 | MidEQ Frequency | 0..127 | numEQMidFrequency |
| 231 | 222 | MidEQ Q-Factor | 0..127 | NumEQQ-factor |
| 232 | 223 | LowEQ Gain | 0..127 | NumEqInDB |
| 233 | 224 | HighEQ Gain | 0..127 | NumEqInDB |
| 234 | 225 | Bass Intensity | 0..127 | unipolarPercentOff |
| 235 | 226 | Bass Tune | 0..127 |  |
| 236 | 227 | Input Ringmodulator | 0..127 | unsignedOff |
| 237 | 228 | Distortion Curve | 0..25 | NameDistortionModes |
| 238 | 229 | Distortion Intensity | 0..127 | unipolarPercent |
| 239 | 230 | B_Undefined102 | 0..127 | unsignedZero |
| 240 | 231 | Assign 4 Source | 0..39 | modmatrixSource |
| 241 | 232 | Assign 4 Destination | 0..127 | modmatrixDest |
| 242 | 233 | Assign 4 Amount | 0..127 | signedMidOff |
| 243 | 234 | Assign 5 Source | 0..39 | modmatrixSource |
| 244 | 235 | Assign 5 Destination | 0..127 | modmatrixDest |
| 245 | 236 | Assign 5 Amount | 0..127 | signedMidOff |
| 246 | 237 | Assign 6 Source | 0..39 | modmatrixSource |
| 247 | 238 | Assign 6 Destination | 0..127 | modmatrixDest |
| 248 | 239 | Assign 6 Amount | 0..127 | signedMidOff |
| 249 | 240 | SingleName0 | 0..127 | ascii |
| 250 | 241 | SingleName1 | 0..127 | ascii |
| 251 | 242 | SingleName2 | 0..127 | ascii |
| 252 | 243 | SingleName3 | 0..127 | ascii |
| 253 | 244 | SingleName4 | 0..127 | ascii |
| 254 | 245 | SingleName5 | 0..127 | ascii |
| 255 | 246 | SingleName6 | 0..127 | ascii |
| 256 | 247 | SingleName7 | 0..127 | ascii |
| 257 | 248 | SingleName8 | 0..127 | ascii |
| 258 | 249 | SingleName9 | 0..127 | ascii |
| 259 | 250 | Filter Select | 0..2 | filterSelect |
| 260 | 251 | Category1 | 0..22 | category |
| 261 | 252 | Category2 | 0..22 | category |
| 262 | 253 | B_Undefined125 | 0..127 | unsignedZero |
| 263 | 254 | B_Undefined126 | 0..127 | unsignedZero |
