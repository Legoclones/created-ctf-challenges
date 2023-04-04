# More Pain
Level: Medium

Description:
```
Your goal is to get the flag hidden in the file system! Can you outsmart us?? The password is `CosmoCougar!`.

`ssh byuctf@byuctf.xyz -p 40000`
```

## Writeup
The flag is stored in `-𝓡/-𝑹`. Using the `--` command can allow you to treat file and directory names as not arguments (ie, `cd -- -𝓡` will work).

**Flag** - `byuctf{i_hope_you_learned_stuff}`

## Hosting
This challenge should be a Docker container that runs an Ubuntu instance that can be accessed through SSH on port 40000. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t morepain .
```

The command to start the challenge is:

```bash
sudo docker run -p 40000:22 --detach --name morepain morepain:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop morepain
```
