# Argument
Description:
```
I just wanted to make a simple application where people can store files. But I'm a good college student and have taken web security classes, so I'm aware of all the vulnerabilities that may exist and made my app perfectly secure! There's no way you'd be able to get the flag...

https://argument.chal.cyberjousting.com

[argument.zip]
```

## Writeup
The vulnerability in the application is actually argument injection through the `tar *` command being run, which is kind of hard to find. One may think it's bypassing the UUID check, XSS, or other file vuln, but it's not. Uploading a file called `--checkpoint=1` and another called `--checkpoint-action=exec=whoami` will call the command `whoami` to be run when `tar *` is executed. However, the filter that prohibits `..` and `/` from being in the filename presents itself as somewhat of a nuisance, so doing a simple `echo 'base64content' | base64 -d | bash` will allow you to bypass that filter. This takes two steps, one to find the flag filename, and the other to read the contents of the flag.

**Flag** - `byuctf{argument_injection_stumped_me_the_most_at_D3FC0N_last_year}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 40000. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```