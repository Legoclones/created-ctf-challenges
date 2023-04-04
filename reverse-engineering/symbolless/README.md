# Symbolless
Level - Medium

Description:
```
I recently learned that you can remove all symbols in a binary.

[symbolless]
```

## Writeup
When you put the executable in Ghidra, you get an `entry()` function and a bunch of unnamed functions with it. Inside of `entry()`, you see the line `FUN_00402a10(param_1,param_2,param_3,param_4,param_5,param_6,param_7,param_8,FUN_004016a5,in_stack_00000000,(long *)&stack0x00000008,0,0,param_11,auStack8);`. If you go to `FUN_004016a5()` (one of the parameters), you'll see a fairly understandable decompilation of what was the `main()` function. It takes each of the hex values defined and XORs it with `0x14` to get the flag.

The hardest part of the reverse engineering process is finding the function, since it's statically-linked (so all relevant library functions are included in the executable), and the symbol table is removed (so all functions are unnamed). 

**Flag** - `byuctf{remov1ng_symb0l_table5_is_4_comm0n_rev_tr1ck}`

## Notes
`symbolless` was compiled with the command `gcc -o symbolless symbolless.c -static -static-libgcc -static-libstdc++ && strip --strip-all symbolless`