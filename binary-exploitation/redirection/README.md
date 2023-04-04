# Redirection
Level - Hard

Description:
```
Well, apparently someone had snuck a `win()` function in my last program, so I decided to take it out this time. Good luck!

nc byuctf.xyz 40003

[redirection]
```

## Writeup
**Purpose** - here, we see that the flag is read into a variable but will only be printed out if 1 == 2 (which is impossible). However, if we can figure out how to run the line that will print out the flag, we can get it! Flow redirection!

**Vulnerability** - same as `ret2win`, the buffer that stores your name can be overflowed

**Roadblocks** - same as `ret2win`:
```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
```

### Exploit
Our script is going to look very similar to the one for ret2win. The only two differences are 1) the garbage padding, and 2) the return address. When we inspect the `redirection` binary in Ghidra, we can see that the address for the lines of assembly that load the flag and run `printf` is `0x401248`. Also, we now have two variables that store the contents of `1` and `2`, which are compared to give us our impossible condition. Since both variables are integers, and integers are 8 bytes, that means our garbage padding from `ret2win` needs to be increased by 16 bytes (0x10 bytes), so our total garbage padding will be `0x38` instead of `0x28`.

Running it, we get the output:
```
[*] '/tmp/redirection'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process '/tmp/redirection': pid 4807
[*] Switching to interactive mode
Enter your name: Your flag is - byuctf{flow_redirection_is_similar_to_ret2win}
Enter your name: $
[*] Interrupted
[*] Stopped process '/tmp/redirection' (pid 4807)
```

**Flag** - `byuctf{flow_redirection_is_similar_to_ret2win}`

## Hosting
The binary `redirection` was compiled with `gcc -o redirection redirection.c -no-pie`.

This challenge should be a Docker container that runs the executable `redirection` every time someone connects on port 40003. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t redirection .
```

The command to start the challenge is:

```bash
sudo docker run -p 40003:40000 --detach --name redirection redirection:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop redirection
```