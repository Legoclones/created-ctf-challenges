# Roblox
Level - Easy

Description:
```
I've returned to my earlier days and have decided to start creating and using Roblox hacks. However, to make sure I don't get caught, I've put a login page on my server so that only I can access my data. Can you get the admin credentials?

nc byuctf.xyz 40000
```

## Writeup
This problem is a variant of SQL injection, except it's code injection. You can either take the boolean-based approach where you use a password payload like `"+users[0]["password"][:1] == "a") and (user["password"]+"` and brute force it letter by letter, or you can take the more intuitive approach and just insert your own code that you know will be executed - `"+print(user)+"`. 

**Flag** - `byuctf{th1s_1s_th3_cous1n_of_sql1}`

## Hosting
This challenge should be a Docker container that runs the python script `roblox.py` every time someone connects on port 40000. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t roblox .
```

The command to start the challenge is:

```bash
sudo docker run -p 40000:40000 --detach --name roblox roblox:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop roblox
```