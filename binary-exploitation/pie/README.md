# Pie
Level - Hard

Description:
```
The roundest knight at King Arthur’s table was Sir Cumference. He ate too much pi.

nc byuctf.xyz 40004

[pie]
```

## Writeup
**Purpose** - the purpose here is the same as ret2win - call the `win()` function to get the flag!

**Vulnerability** - same as `ret2win`, the buffer that stores your name can be overflowed

**Roadblocks** - here, our roadblocks are a little bit different:
```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      PIE enabled
```

PIE is enabled, which means that we don't know where the `win()` function will be since ASLR randomizes where it is each time. In order to figure out where it's stored in memory, we need an **info leak**. An info leak means we somehow get an address for something in the same memory space as the `win()` function. Luckily, the executable is very nice and prints out the location of the `vulnerable()` function for us! So if we write our Python script to read in the address of `vulnerable()`, and then add/subtract the difference between that and the `win()` function (which is constant), we can redirect our buffer overflow to return to `win()`!

## Exploit
For my solve script, I went ahead and copied `solve.py` from our `ret2win` problem earlier and made a few adjustments. First, I added a line that will run `p.recvline()` to save the line that prints out our info leak, and parsed it to pull out just the address. I then calculated the difference between the start of the `vulnerable()` function and the start of the `win()` function to be 0x87 bytes off, and print out where the `win()` function should be located in memory. 

The last part is the same, we send 0x28 bytes of garbage and then the memory address of where we want to go to accomplish our buffer overflow.

Running it, we get the output:
```
[*] '/tmp/pie'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
[+] Starting local process '/tmp/pie': pid 1873
Win is at: 0x55aa3a7dd1ec
[*] Switching to interactive mode
Enter your name: [*] Process '/tmp/pie' stopped with exit code 0 (pid 1873)
Your flag is - byuctf{all_you_need_to_bypass_PIE_is_an_infoleak}
[*] Got EOF while reading in interactive
```

(*Note - the script only works like 75% of the time. Sometimes it doesn't randomly work \o/ idk why, just do it again*)

**Flag** - `byuctf{all_you_need_to_bypass_PIE_is_an_infoleak}`

## Hosting
`pie` was compiled with `gcc -o pie pie.c`.

This challenge should be a Docker container that runs the executable `pie` every time someone connects on port 40004. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t pie .
```

The command to start the challenge is:

```bash
sudo docker run -p 40004:40000 --detach --name pie pie:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop pie
```