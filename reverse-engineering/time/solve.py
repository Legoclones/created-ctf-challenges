from pwn import *
import subprocess


binary = "src/time"
elf = context.binary = ELF(binary, checksec=False)

if args.REMOTE:
    p = remote("time.chal.cyberjousting.com", 1337)
elif args.REMOTE2:
    p = remote("localhost", 40003)
else:
    p = elf.process()

# get numbers and decrypt by seeding at the same time
numbers = p.recvline()[12:].strip().decode()
print(numbers)
print(subprocess.getoutput(f"./solve \"{numbers}\""))

p.close()