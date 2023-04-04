# Start
Level - Easy

Description:
```
What address is `main()` located at?

Flag format - `byuctf{0x000000}`

[start]
```

## Writeup
This executable was compiled on a Raspberry Pi, so it's a 32-bit ARM executable. PIE is also disabled on the executable, so the start address of the binary is known. It's normally `0x400000` for 64-bit AMD executables, but is `0x010000` for 32-bit ARM executables. Opening this binary in GDB will reveal the address.

**Flag** - `byuctf{0x0103d0}`

## Hosting
Compiled with `gcc -o start start.c -no-pie` on a Raspberry Pi, bullseye release.