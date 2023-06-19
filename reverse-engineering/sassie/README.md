# Sassie
Level - Hard

Description:
```
Don't give me that attitude! I can be sassy if I want!

[sassie]
```

## Writeup
This binary has the symbol table stripped and strings are dynamically created. It generates some strings used, checks for GDB processes, checks to make sure the file `/tmp/tmpt2nxegs1` exists and the MD5 hash of the contents make it lol, then dynamically creates shellcode in the memory range 0x54551300000 that writes some bytes to 0x54551300300, generates more shellcode, and runs the shellcode that XORs 0x54551300300 with a key to put the flag on the stack. It then uses a syscall to exit.

The intended solution is to skip over the alarm and GDB checks, write `lol` to `/tmp/tmpt2nxegs1`, then step through the shellcode being run until the flag appears on the stack.

**Flag** - `byuctf{sorry_f0r_b31ng_545513}`

## Hosting
`sassie` was compiled with `gcc -o sassie -fstack-protector-all sassie.c md5.c` (yes PIE, yes stack canaries), then stripped with `strip -s sassie`.