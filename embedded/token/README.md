# Token
Description:
```markdown
While doing hacking our router, we found a buffer overflow that had to be exploited in conditions similar to these ones. If you've never learned MIPS, now is the time!

`nc token.chal.cyberjousting.com 1354`

[token.zip]
```

## Writeup
This challenge involves sending an AES-ECB-encrypted payload to exploit a buffer overflow (ret2system) in a 32-bit, little-endian MIPS binary hosted with qemu. The code was compiled with a [uClibc buildroot toolchain](https://buildroot.org/download.html), and is being hosted with a patched version of qemu that supports ASLR. 

The binary protections are as follows:
```
Arch:     mips-32-little
RELRO:    Full RELRO
Stack:    No canary found
NX:       NX unknown - GNU_STACK missing
PIE:      No PIE (0x400000)
Stack:    Executable
RWX:      Has RWX segments
```

Reversing the binary will reveal that a random AES key is generated and sent to the client. The server then waits for an encrypted message from the client, and once it receives it, it decrypts it, checks the header, and throws it into `parse()`. The header is only 15 bytes, and only 4 of those bytes are checked. The incoming encrypted data, instead of being saved on the stack, is actually saved in a global variable, which is important. 

Inside `parse()`, the decrypted string is separated based on the `&` delimiter, looking for sections `t=` and `tz=` (any section that doesn't will error out). The token (`t=`) variable is saved into a 16-byte buffer using `sscanf("%s")`, which doesn't check the length of the string. This is where the overflow is. 

### Roadblocks
A normal pwn practitioner would think "Alright, let's just do some ROP", but this is where it gets tricky. MIPS doesn't have a `return` instruction. `return` is basically just "pop the top off the stack and go to it"; in MIPS, this is implemented by popping off `stack+0xoffset`, `stack += offset`, then `jmp $ra` (jump to the return address register). This slight change drastically decreases (if not completely eliminates all) the ROP gadgets available. Controlling `$pc` once is easy, but controlling it after that is very difficult. So what we need is a one-shot. 

Luckily, our program runs `system()` inside a logging function, and we can use that to our advantage. At address `0x40104c`, our program executes `system($s8+0x18)`; if we can point the `$s8` (also known as the `$fp`, or frame pointer register), which is the MIPS equivalent of `$rbp`, to a user-controlled memory address, then we can pop a shell!

But where can we point it? ASLR is enabled, so we don't know where any libraries or the stack are present, and there are no info leaks (hopefully!) in the binary. However, PIE is disabled so we know all the addresses of global variables, and luckily we control one - `input_buf`! But wait, doesn't that have to be encrypted? Well, it uses AES-ECB-128, which decrypts input in blocks of 16 at a time, not reliant on previous blocks. As long as you stick a block of 16 bytes at the end of your regular encrypted endpoint, it can be anything you want as long as you don't care that when "decrypted" it will be garbage.

Next problem - we need to set both `$s8` and `$ra` with 32-bit addresses, and both addresses have a null byte in them, but we're using `sscanf("%s")`, which will stop once a null byte happens. For `$ra`, we can just overwrite the first 3 bytes and keep the last byte the same (null), but we need a workaround for setting `$s8`. Luckily, `sscanf("%s")` will place a null byte at the end of our string for us, and our token set inside a loop. We can put a token in there twice, and have the first token be `padding + garbage_s8 + ra_value`, and our second token be `padding + s8_value`, and the `sscanf()` function will place a single null byte after our 3 bytes of `s8_value`. Upon return, our exploit chain should work!

### Final Exploit
Here's a quick summary of our exploit:
* Retrieve the randomly-generated AES encryption key
* Create a fake 15-byte header with the 4 checked bytes in it
* Create a payload that sets `t=` twice. 20 bytes of padding are needed. 
    * Our first token will overwrite the stored `$s8` value on the stack with garbage, then write the 3 least-significant bytes of the saved `$ra` register with `0x40104c` (the address of our `system()` gadget).
    * Our second token will have 20 bytes of padding and overwrite the stored `$s8` value with 3 bytes of `0x41410f` (the address of `"/bin/sh"` - 0x18), letting `sscanf()` place a null byte in the 4th spot.
* This payload is encrypted using AES-ECB-128 with the key retrieved from the server. 
* One more "block" is added to the end - `b'AAAAAAAA/bin/sh\x00'` (giving us our `"/bin/sh"` string)
* Our header + encrypted payload + block are sent to the server, and the binary ends up running `system("/bin/sh")` and we get our shell!

A solve script can be found at [`solve.py`](./solve.py).

**Flag** - `byuctf{re4lly_h4rd_t0_d0_R0P_when_r3turn_d0esn't_ex1st}`

## Hosting
This challenge should be a Docker container that runs the binary `token` on port 40002 each time a user connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```