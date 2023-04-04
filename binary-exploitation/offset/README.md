# Offset
Level - Easy

Description:
```
What is the offset between the `rand` function and `system` function in this `libc` file?

Flag format - `byuctf{0x0000}`

[libc-2.27-2.so]
```

## Writeup
The [solve.py](solve.py) script uses pwntool's built-in functionality to find offsets between the location of functions using the executable's symbol table.

**Flag** - `byuctf{0xb090}`