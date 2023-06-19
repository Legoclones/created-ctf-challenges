# Shellcode
Level - Medium

Description:
```
You'll have to make your own shellcode for this one!

`nc byuctf.xyz 40017`

[shellcode] [shellcode.c]
```

## Writeup
This C file takes in 40 bytes (4 segments of 10 bytes) and runs the ASM built by it, allowing you to put in your own shellcode. I split it up into 4 segments so they couldn't just copy and paste some shellcode somewhere, but had to come up with their own. It may be possible with only 30 bytes too, but I just wanted it to be medium difficulty so they have some bytes to spare. 

My solve script compiles ASM commands into 9 bytes, 9 bytes, 9 bytes, and 4 bytes, sends them, and gets a shell back. It relies on putting `"/bin/sh"` into `$rdi`, setting `$rax = 0x3b`, and `$rdi` and `$rsi` to 0. 

**Flag** - `byuctf{1m_als0_pretty_new_t0_pwn_s0_h0p3_it_was_g00d}`

## Hosting
`shellcode` was compiled with `gcc -o shellcode -fstack-protector-all shellcode.c`.

This challenge should be a Docker container that runs the executable `shellcode` every time someone connects on port 40017. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t shellcode .
sudo docker network create -d bridge shellcode
```

The command to start the challenge is:

```bash
sudo docker run -p 40017:40000 --detach --name shellcode --network shellcode shellcode:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop shellcode
```
