from pwn import *

libc = ELF("./libc-2.27-2.so", checksec=False)

system = libc.symbols['system']
rand = libc.symbols['rand']

print("The offset is",hex(system-rand))