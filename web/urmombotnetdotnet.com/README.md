# urmombotnetdotnet.com 
This is a 5-problem web challenge that uses some Python code developed in one of my classes. A Flask server is run with a MySQL backend, and all challenges use this same infrastructure. A redacted version of the relevant source code should be included in each challenge (`urmombotnetdotnet.com/` directory was zipped into `urmombotnetdotnet.com.zip`).

* [Challenge 1](Chall1.md)
* [Challenge 2](Chall2.md)
* [Challenge 3](Chall3.md)
* [Challenge 4](Chall4.md)
* [Challenge 5](Chall5.md)

## Hosting
This challenge spins up 2 docker containers, one that runs MySQL internally, and a Python Flask server `server.py` on port 40010. All the proper files are included in here. The command to start the challenge is (when located inside of this directory):

```bash
sudo docker compose up -d
```

The command to stop the challenge is:

```bash
sudo docker stop urmombotnetdotnet.com-app urmombotnetdotnet.com-mysql
```