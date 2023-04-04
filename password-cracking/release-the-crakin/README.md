# Release the Crakin
Level - Hard

Description:
```
Instead of creating multiple password cracking challenges, we just decided to stick them all into one challenge and make it hard. Can you get the flag??

`nc byuctf.xyz 40017`
```

## Writeup
Get all the answers right and google the hash to get the password.

**Flag** - `byuctf{flag}`

## Hosting
This challenge should be a Docker container that runs the python script `crakin.py` every time someone connects on port 40017. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t crakin .
```

The command to start the challenge is:

```bash
sudo docker run -p 40017:40000 --detach --name crakin crakin:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop crakin
```