# Notes
Level - Medium

Description:
```markdown
Server - http://byuctf.xyz:40018/

Admin bot - http://byuctf.xyz:40019/

[notes.zip]
```

## Writeup
The goal is to have the bot visit a page of your own to share the note with the flag with you. Since you know the note ID of the flag note (`'0'*32`), you can use an HTML page like `solve.html`, which will automatically fill out a form with the required information and submit it to localhost, which the admin bot has signed into. 

The bug with the CSRF tokens is it checks for one, but it doesn't check who was given the token, nor does it revoke the tokens after a certain amount of time! This means you can just get a token of your own and use it, and the server will be none the wiser!

To do so, follow the steps below:
1. Save `solve.html` and run `python3 -m http.server` in the local directory to have a web server running on port 8000
2. Run ngrok by doing `ngrok http 8000` - it will give you a unique subdomain in the `Forwarding` field.
3. Go to the website and create an account for `legoclones`, and log into it.
4. Go to the admin bot and submit the subdomain given by ngrok + `/solve.html`, like `https://723b-128-187-116-14.ngrok-free.app/solve.html`.
5. When the admin bot visits the page, the form will automatically be submitted and the flag note will be shared with `legoclones`.
6. Back onto the main site, see your list of notes and the flag will show up!

**Flag** - `byuctf{1_thought_th4t_w4s_pretty_cl3v3r}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 40018, and the admin bot portal `admin_bot.js` on port 40019. All the proper files are included in here. The command to build the docker container is (when located inside of this directory):

```bash
sudo docker build -t notes2 .
sudo docker network create -d bridge notes2
```

The command to start the challenge is:

```bash
sudo docker run -p 40018:1337 -p 40019:1336 --detach --name notes2 --network notes2 notes2:latest
```

The command to stop the challenge is:

```bash
sudo docker stop notes2
```