# Collision
Level - Hard

Description:
```
Can you make 2 PNGs with the same MD5 hash, but different pre-defined strings inside of it? Go ahead!

`nc byuctf.xyz 40016`

[verify.py]
```

## Writeup
I used the PNG collision script made by [corkami](https://github.com/corkami/collisions). `pic1.png` and `pic2.png` are the two base "PNGs" that I used. To generate `collision1.png` and `collision2.png` (that meet the requirements), I just ran `png.py pic1.png pic2.png`. 

**Flag** - `byuctf{c0ll1s10n5_4r3_c00l10}`

## Hosting
This challenge should be a Docker container that runs `python3 verify.py` on port 40016. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t collision .
sudo docker network create -d bridge collision
```

The command to start the challenge is:

```bash
sudo docker run -p 40016:40000 --detach --name collision --network collision collision:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop collision
```