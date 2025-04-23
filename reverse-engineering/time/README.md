# Time
Description:
```markdown
I tick but never tock,
I age but never grow old,
I'm always moving, never still,
What am I that time can't hold?

`nc time.chal.cyberjousting.com 1355`

[time]
```

## Writeup
If you use something like pwntools and start up a solve script at the same time, then when you seed your solve script it will have the same numbers and can XOR the given numbers to get the flag. This is automated in `solve.py`, which uses `solve.cpp`. The docker container may have a unix timestamp a few seconds off, so a bit of brute force is needed to get the flag from it, but it shouldn't be too hard. That is not in `solve.py` currently but should work.

**Flag** - `byuctf{ooooooooh_a_seeded_PRNGGGGGGGGGG}`

## Hosting
`time` was compiled with the command `g++ -o time time.cpp`.

This challenge should be a Docker container that runs the binary `time` on port 40003 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```