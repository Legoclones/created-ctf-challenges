# Roblox2
Level - Medium

Description:
```
Hmm it appears there was a vulnerability! I've made some changes though, so I don't think it'll show you anything anymore...

nc byuctf.xyz 40005
```

## Writeup
The error doesn't appear anymore, but the actual source code hasn't changed. Instead, the flag is located in `flag.txt` and RCE must be used to find and read it. This payload should work -  `"+__import__("os").system("cat flag.txt")+"`. Note that the word "open" also can't be in the payload, or else it will exit early!

**Flag** - `byuctf{1_h0p3_y0u_3nj0y3d_th3_ch4ll3ng3_:)}`

## Hosting
This challenge should be a Docker container that runs the python script `roblox2.py` every time someone connects on port 40005. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t roblox2 .
```

The command to start the challenge is:

```bash
sudo docker run -p 40005:40000 --detach --name roblox2 roblox2:latest
```

The command to stop the challenge is:

```bash
sudo docker stop roblox2
```