# numbersss
Description:
```markdown
Sometimes computer numbers can be so harddd

`nc numbersss.chal.cyberjousting.com 1351`

[numbersss] [Dockerfile]
```

## Writeup
If you put in a negative number, it will pass the check but allow you to put in 128+ characters, leading to a buffer overflow. A libc leak is given for Ubuntu 23.04, which they may miss if they don't check. They can then make a ROP chain to execute `system("/bin/sh")` and get the flag. See `solve.py`.

**Flag** - `byuctf{gotta_pay_attention_to_the_details!}`

## Hosting
`numbersss` was compiled with the command `gcc -fno-stack-protector -no-pie -o src/numbersss numbersss.c`.

This challenge should be a Docker container that runs the binary `numbersss` on port 40003 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```