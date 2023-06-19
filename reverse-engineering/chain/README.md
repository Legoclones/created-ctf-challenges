# Chain
Level - Easy/Medium

Description:
```
You know sometimes you just run out of ideas for challenge descriptions...

[chain]
```

## Writeup
This binary takes in a 44-character password (flag), XORs it with some values, and compares it to another array of ints. The array of values is calculated by taking a base address (`0x105ac`) and an array of offsets, then pulling the value from that memory address, and XORing it with the password char to match the int array.

To reverse engineer, you can use the base address + array of offsets to find the hex values, then XOR that with the static array `correct` to retrieve the flag.

**Flag** - `byuctf{1_h0p3_ARM_wasn't_t00_b4d_0f_4_tw1st}`

## Hosting
`chain` was compiled with `gcc -o chain -fstack-protector-all chain.c` (no PIE, yes stack canaries) on a Pi, then stripped with `strip -s chain`.