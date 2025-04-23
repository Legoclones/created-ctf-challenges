from pwn import *
context.update(arch='mips', os='linux', bits=32, endian='little')
shellcode = asm('''
li $ra, -1
li $v0, -1
li $v1, -1
li $a0, -1
li $a1, -1
li $a2, -1
li $a3, -1
li $t0, -1
li $t1, -1
li $t2, -1
li $t3, -1
li $t4, -1
li $t5, -1
li $t6, -1
li $t7, -1
li $t8, -1
li $t9, -1
li $s0, -1
li $s1, -1
li $s2, -1
li $s3, -1
li $s4, -1
li $s5, -1
li $s6, -1
li $s7, -1
li $s8, -1
li $gp, -1
''')

print(shellcode)
print(len(shellcode))

tmp = ''.join([ '\\x%02x' % x for x in shellcode ])

for i in range(len(tmp)):
    print(tmp[i], end='')
    if i % 16 == 15:
        print()


### RUN SHELLCODE ###
filename = make_elf(shellcode, extract=False)

gs = """
break *(vuln+169)
continue
"""
if args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(filename, gdbscript=gs)
else:
    p = process(filename)
p.interactive()