# Jukebox
Level: Easy

Description:
```
Can you break our jukebox and get the flag??

`nc byuctf.xyz 40001`
```

## Writeup
If you type in a non-integer, integer over 5, or integer under 0, we'll catch it. However, entering `0` is not caught and will throw an error. The flag is the function name!

**Flag** - `byuctf{th1s_1s_y0ur_fl4g}`

## Hosting
This challenge should be a Docker container that runs the python script `jukebox.py` every time someone connects on port 40001. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t jukebox .
```

The command to start the challenge is:

```bash
sudo docker run -p 40001:40000 --detach --name jukebox jukebox:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop jukebox
```