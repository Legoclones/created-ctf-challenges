# MIPScode
Description:
```markdown
An important part of binary exploitation is the ability to make shellcode that conforms to your situation. Can you pass both levels to claim the flag?

`nc mipscode-level1.chal.cyberjousting.com 1356`

`nc mipscode-level2.chal.cyberjousting.com 1357`

[mipscode.zip]
```

## Writeup
This challenge involves writing 32-bit, little-endian MIPS shellcode twice. The first shellcode has a maximum of 32 bytes but no null byte/whitespace restrictions, and you need to pop a shell. The second shellcode has a maximum of 44 bytes, but can't contain null bytes or whitespace. The length requirements is shorter than any shellcode you'll see online; in other words, all MIPS shellcode online to pop shells is longer than the requirements. This will force them to write the shellcode by hand to reach the character limit and pop a shell. 

Once the first shellcode is delivered, they need to read out `/ctf/pwd_next.txt` to get the password for level 2. When you reach out to level 2, if you provide an incorrect password, you cannot proceed to the challenge. 

To ensure they don't have any helpers that will allow them to "cut corners" on their shellcode, ASLR is enabled and the shellcode is placed in a custom mmapped RWX section just after the stack that is `memset` with `0xff` bytes (so no null bytes already there). I had hoped to also make challenges requiring the second argument in `execve()` to NOT be NULL, but I couldn't find a way to do that without compiling my own kernel with a patched syscall. 

The solutions for each one is contained in `levelX/solve.py`.

**Flag** - `byuctf{if_i_had_to_do_it_you_have_to_also}`

## Hosting
This challenge should be a Docker container that runs the binary `mipscode_level1` on port 40004 and `mipscode_level2` on port 40005 each time a user connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```