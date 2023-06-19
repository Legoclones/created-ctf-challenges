# Leet 1
Level - easy

Description:
```
Just make 1337

nc byuctf.xyz 40000

[leet1.py]
```

## Writeup
The following solution works - `ord('Թ')` (and there are probably lots of others too, including `print(FLAG)`)

**Flag** - `byuctf{simple_bypasses!}`

## Hosting
This challenge should be a Docker container that runs the Python script `leet1.py` every time someone connects on port 4000x. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t leet1 .
sudo docker network create -d bridge leet1
```

The command to start the challenge is:

```bash
sudo docker run -p 40000:40000 --detach --name leet1 --network leet1 leet1:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop leet1
```