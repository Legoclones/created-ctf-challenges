# Overflow
Level - Medium

Description:
```
Please don't enter the Declaration of Independence.

nc byuctf.xyz 40001

[overflow]
```

## Writeup
This is a very simple buffer overflow. The `vulnerable()` function takes in 64 characters and fits it in a buffer with only 0x30 bytes of space. This means that the extra characters will overflow into the stack. The item just above the buffer is the `key` variable, which is initially set to 0xc. If you put in 60 garbage characters followed by `1234`, then the buffer will be filled and the last four characters will set the value of `key` to 0x34333231. This allows us to run the `win()` function and get the flag. 

Example:
```
$ ./overflow
Enter a text please: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1234
Your flag is - byuctf{s1mpl3_0verfl0w_bug}
```

**Flag** - `byuctf{s1mpl3_0verfl0w_bug}`

## Hosting
`overflow` was compiled with `gcc -o overflow overflow.c`.

This challenge should be a Docker container that runs the executable `overflow` every time someone connects on port 40001. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t overflow .
```

The command to start the challenge is:

```bash
sudo docker run -p 40001:40000 --detach --name overflow overflow:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop overflow
```