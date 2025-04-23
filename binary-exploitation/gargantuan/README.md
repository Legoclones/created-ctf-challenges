# Gargantuan
Description:
```markdown
This beast of a program can take in massive amounts of inputs and store them without any problems, so I decided to call it "Gargantuan"! You wanna test it out?

`nc gargantuan.chal.cyberjousting.com 1352`

[gargantuan] [libc.so.6]
```

## Writeup
This problem leverages a buffer overflow to exploit a partial overwrite (and get EXE leak), exploit ret2plt (to get a libc leak), and run a ROP chain to ret2libc (requiring a triple exploit). The buffer overflow occurs because the `tmp` buf (size 0x200) is being copied into `storage` buf, but the check is done with `strlen`. Since you can put a null byte anywhere in the middle of your payload, it will pass the check, but transfer ALL bytes into storage, leading to an overflow. The padding/socket communication is pretty tricky, but a working solution is at `solve.py`.

**Flag** - `byuctf{I_wanted_to_make_buffer_sizes_bigger_but_the_network_didnt_agree}`

## Hosting
`gargantuan` was compiled with the command `gcc -fno-stack-protector -o src/gargantuan gargantuan.c`.

This challenge should be a Docker container that runs the binary `gargantuan` on port 40004 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```