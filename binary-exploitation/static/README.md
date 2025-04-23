# Static
Description:
```markdown
So I heard all about these binary exploitation attacks involving libraries and libc, and that's got me worried! I decided to statically compile all of my binaries to avoid those attack vectors. This means I don't need to worry about mitigations, right?

Right??

`nc static.chal.cyberjousting.com 1350`

[static]
```

## Writeup
Yes, `checksec` says there are canaries. No, there are no canaries on functions like `main()`. This requires forming a ROP chain to spawn a shell using `syscall` after exploiting the obvious overflow. The hardest part of the ROP chain is figuring out how to put `"/bin/sh"` in `$rdi`. The approach I chose to take was take a known writable address (`0x4a0000` since PIE is disabled), write `"/bin/sh"` there, and put that address into `$rdi`. Putting it on the stack is really difficult and gadgets aren't super conducive.

The ROP chain takes 118 bytes (w/out the padding) and successfully spawns a shell on the target system. The gadgets, locations, and how the ROP chain is formed is automated and commented in `solve.py`.

**Flag** - `byuctf{glaD_you_c0uld_improvise_ROP_with_no_provided_gadgets!}`

## Hosting
`static` was compiled with the command `gcc -fno-stack-protector -o src/static -static -no-pie static.c`.

This challenge should be a Docker container that runs the binary `static` on port 40002 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```