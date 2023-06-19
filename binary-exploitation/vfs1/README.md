# VFS1
Level - Medium

Description:
```
I've decided that we don't virtualize things enough, so I created a virtual file system that you can run and save your secrets on. This is still in beta-testing, but let me know what you think!

`nc byuctf.xyz 40008`

[vfs] [vfs.c]
```

## Writeup
This binary has been compiled with all 4 main security measures, but the main vulnerability relies on where content is grabbed and placed into the filesystem. When copying content into the filesystem, null bytes aren't taken into account. This means that the 10th file can go to the end of the filesystem, and null byte exists between the contents and file. When the last file is read, the flag is also printed at the end of it. The solve script is in `solve.py`.

**Flag** - `byuctf{more_like_VULNERABLE_file_system!}`

## Hosting
`vfs1` was compiled with `gcc -o vfs1 -fstack-protector-all vfs1.c`.

This challenge should be a Docker container that runs the executable `vfs1` every time someone connects on port 40008. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t vfs1 .
sudo docker network create -d bridge vfs1
```

The command to start the challenge is:

```bash
sudo docker run -p 40008:40000 --detach --name vfs1 --network vfs1 vfs1:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop vfs1
```