from pwn import *
from hashlib import md5

if args.REMOTE:
    p = remote("protocol.youcanhack.me", 1337)
else:
    p = process(["python3", "server.py"])


### FLAG ###
DBG_MSG = b'pls gimme fleg'
DBG_HASH = md5(DBG_MSG).digest()
LEN = len(DBG_MSG) + len(DBG_HASH)
p.sendline(b'\xff\x00\x00'+b"\xc0\x00\x00"+b'\x67'+LEN.to_bytes(2, 'little')+DBG_MSG+DBG_HASH)
print(p.recvall()[18:])
p.close()