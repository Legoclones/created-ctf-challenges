# Ducky3
Level - Medium

Description:
```
Alright fine, I'll make my own keyboard layout...

[inject.bin] [payload.txt]
```

## Writeup
At this point, the decoder scripts are completely useless. Since I've printed out the entire alphabet in the strings before, it's simply a matter of matching up the letters to the opcodes, and then figuring out what the flag is at the end. `byuctf.json` is the keyboard layout used to generate the `inject.bin` file from the payload, and `mixup.py` was used to generate `byuctf.json`.

**Flag** - `byuctf{1_h0p3_y0u_enj0yed-thi5_very_muCH}`