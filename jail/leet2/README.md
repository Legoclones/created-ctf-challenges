# Leet 2
Level - easy

Description:
```
Just make 1337 (again)

nc byuctf.xyz 40001

[leet2.py]
```

## Writeup
The following solution works - `0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf+0xf-0xd`

**Flag** - `byuctf{aaaaaaand_more_simple_bypasses_:)}`

## Hosting
This challenge should be a Docker container that runs the Python script `leet2.py` every time someone connects on port 40001. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t leet2 .
sudo docker network create -d bridge leet2
```

The command to start the challenge is:

```bash
sudo docker run -p 40001:40000 --detach --name leet2 --network leet2 leet2:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop leet2
```