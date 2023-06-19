# Frorg
Level - Hard

Description:
```
I love arnimals like frorggies and crarbs and octurpurse

`nc byuctf.xyz 40015`

[frorg] [libc.so.6]
```

## Writeup
This simple C binary was compiled without PIE and stack canaries, allowing a buffer overflow -> ret2libc to occur. However, due to the weird way it's reading in input, you have to be careful when overwriting the value for `i` so your input is contiguous. Because there's no limit on what `i` can be, you can overwrite the buffer storing frorgy names. You utilize the overflow to first leak the address of libc using PLT, and loop back to `main` to exploit again. The second time, you use the offset of libc to calculate the address of the string `"/bin/sh"` and the function `system` to pop a shell.

This process is automated in `solve.py`.

**Flag** - `byuctf{fr0rg13s_s4y_rib1t_rib1t}`

## Hosting
`frorg` was compiled with `gcc -o frorg -no-pie -fno-stack-protector frorg.c`.

This challenge should be a Docker container that runs the executable `frorg` every time someone connects on port 40015. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t frorg .
sudo docker network create -d bridge frorg
```

The command to start the challenge is:

```bash
sudo docker run -p 40015:40000 --detach --name frorg --network frorg frorg:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop frorg
```