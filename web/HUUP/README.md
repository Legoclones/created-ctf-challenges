# HUUP
Description:
```markdown
There's all this rage around TCP, but I think UDP is superior, so I made my website only accessible through UDP!

*Notes - max message length is 1024 bytes, only GET requests will really work, and messages are discarded after 10 seconds*

`byuctf.xyz:40011`
```

## Writeup
This is one of my favorite challenges! In the Docker container, I run the website normally using Flask, but made a Python middleware called `udp_server.py` that listens on port 40000 for incoming text. This server will forward requests once a `'\r\n\r\n'` is found to the actual web server, and send the response back to the client. Because this is UDP, there's a high chance that only the headers and not the actual content body will be returned (like 80% chance). This means that you have to send the same HTTP request multiple times until you get one with the actual body. 

To solve, you need to access `/`, which will direct you to try the endpoints at `/endpoints.txt`. This endpoint returns a list of 200 possible endpoints, and it's brute force from there. 3 false positives will return with a 200 OK response, and one has the flag. A solve script (`solve.py`) was written to send a raw HTTP request over UDP to the specified domain/port, and send it over and over until it does not return with a `'\r\n\r\n'` at the end (meaning the content body was actually included). This can then be automated to get the endpoints, parse, and try each one until the flag is found!

**Flag** - `byuctf{there's_a_reason_we_do_HTTP_over_TCP_fc163467}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 1337, and `udp_server.py` on port 40011. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t huup .
sudo docker network create -d bridge huup
```

The command to start the challenge is:

```bash
sudo docker run -p 40011:40000/udp --detach --name huup --network huup huup:latest
```

The command to stop the challenge is:

```bash
sudo docker stop huup
```