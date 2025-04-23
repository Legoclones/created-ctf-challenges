# Directory
Description:
```markdown
Have so many friends, you forget what their names are? Here's a cool little app I made for you where you can record their names!

`nc directory.chal.cyberjousting.com 1349`

[directory.zip]
```

## Writeup
You need to put in 9 fake strings and the tenth one will overflow into the `$rip` pointer. Since PIE is enabled, you'll need to use a partial overwrite to return to the `win()` function.

**Flag** - `byuctf{yeeee3e3e3_p4rt14l_0v3rwr1t3!!}`

## Hosting
`directory` was compiled with the command `gcc -fno-stack-protector -o src/directory directory.c`.

This challenge should be a Docker container that runs the binary `directory` on port 40001 each time someone connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```