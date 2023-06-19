# PBKDF2
Level - Medium

Description:
```
Can you unzip the file to get the flag??

http://byuctf.xyz:40009

[Dockerfile] [server.js] [package.json]
```

## Writeup
A while ago, I came across an article talking about how [ZIP files can have 2 passwords](https://www.bleepingcomputer.com/news/security/an-encrypted-zip-file-can-have-two-correct-passwords-heres-why/). If a password is over 64 characters long, the ZIP utility will instead take the SHA1 hash and use that as the password instead. This means that both the password AND the SHA1 hash are valid. 

To implement that, I make a Docker container that uses the password `isnt-byuctf-one-of-your-most-favorite-ctfs-even-though-this-is-only-our-second-year-3HF4z` to zip the flag file. I also created a simple NodeJS server that unzips it with the password provided, however the original password is not allowed! To solve, use the ASCII (not hex) representation of the flag as the password - `:h;V4\%T2EV(@~]Y62$8` (`http://localhost/?password=:h;V4\%T2EV(@~]Y62$8`). I found a password with an ASCII-printable representation using the `calculate.py` file attached.

**Flag** - `byuctf{th4nk_y0u_4rs3n1y_sh4r0g14z0v}`

## Hosting
This challenge should be a Docker container that runs `node server.js` to expose the webserver on port 40009. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t pbkdf2 .
sudo docker network create -d bridge pbkdf2
```

The command to start the challenge is:

```bash
sudo docker run -p 40009:8080 --detach --name pbkdf2 --network pbkdf2 pbkdf2:latest
```

The command to stop the challenge (since CTRL+C won't work) is:

```bash
sudo docker stop pbkdf2
```