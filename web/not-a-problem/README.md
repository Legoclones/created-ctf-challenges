# Not a Problem
Description:
```markdown
Bug bounty hunter: "There's command injection here"

Triager: "But it's only accessible by admins so it's nOt A vUlNeRaBiLiTy"

You: *bet*

Server - https://not-a-problem.chal.cyberjousting.com/

Admin bot - https://not-a-problem-admin.chal.cyberjousting.com/

[not-a-problem.zip]
```

## Writeup
This vulnerability chains requires you to XSS the admin and have the JS payload exploit the command injection to exfil the flag from the filesystem. The `/api/stats/<id>` endpoint is vulnerable to XSS because the proper Content-Type is not being set and the usernames aren't filtered. This is automated in `solve.py`.

**Flag** - `byuctf{"not_a_problem"_YEAH_RIGHT}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 40001, and the admin bot portal `admin_bot.js` on port 40002. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```