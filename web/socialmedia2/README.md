# Social Media 2
Level: Extreme

Description:
```
Well.... that was awkward! It turns out version 1.0 *was* vulnerable, but don't worry - we've figured out a solution! Now you'll never be able to XSS us!

Site - http://byuctf.xyz:40007

Admin bot - http://byuctf.xyz:40008
```

## Writeup
Same as Social Media, except there is a filter in place, so any case-insensitive text with `script`, `onerror`, or `onload` will not work!

**Flag** - `byuctf{m4ny_4ppl1c4t1ons_w1ll_h4ve_f1lters}`

## Hosting
The main website can be spun up by running `python3 unhackable2.py` from the local directory. The admin bot uses a Docker container that makes a webserver that can be accessed port 40008. All the proper files are included in here. The command to build the docker container is (when located inside of the `admin-bot` directory):

```bash
sudo docker build -t adminbot2 .
```

The command to start the challenge is:

```bash
sudo docker run -p 40008:1337 --detach --name adminbot2 adminbot2:latest
```

The command to stop the challenge (since `CTRL+C` won't work) is:

```bash
sudo docker stop adminbot2
```