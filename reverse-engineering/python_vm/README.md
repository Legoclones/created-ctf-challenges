# Python VM
Level - Medium

Description:
```
I love assembly so much, I decided to make my own!

[vm.py] [instructions.bin]
```

## Writeup
The nice-looking version of `vm.py` is found in `vm_orig.py`, not provided to the participants. Custom opcodes and a stack are defined in the Python file. I used `create.py` to create my instructions to check the flag. The first byte of `instructions.bin` is the length of the flag, and the rest are opcodes. 

The solution is to figure out what each opcode does and print debugging statements as `vm.py` processes the `instructions.bin` file, showing what each of the values should be in the flag.

**Flag** - `byuctf{vms_just_1mplem3nt_0pcodes_&_instruct10n5}`