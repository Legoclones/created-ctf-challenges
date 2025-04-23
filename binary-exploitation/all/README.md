# All
Description:
```markdown
What if I just.... put ALL the vulnerabilities in there? With no mitigations?

`nc all.chal.cyberjousting.com 1348`

[all.zip]
```

## Writeup
You are given a large overflow + printf in a loop with no mitigations, but also no syscall/system gadgets. So your options are:

* printf write
* leak a stack pointer and shellcode
* leak a libc pointer and make a ROP chain

I chose the second options and automated it in `solve.py`.

**Flag** - `byuctf{too_many_options_what_do_I_chooooooose}`

## Hosting
`all` was compiled with the command `gcc -fno-stack-protector -o src/all -no-pie -z execstack all.c`.

This challenge should be a Docker container that runs the binary `all` on port 40000 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```