# Random
Description:
```
I've only had the time to make the API, but it should be working properly. Please make sure it's secure. If you can read any file you want, I'll make sure to reward you!

https://random.chal.cyberjousting.com/

[random.zip]
```

## Writeup
There are a couple steps required to get the flag here. First, a JWT needs to be spoofed by discovering the `APP_SECRET` value through the relative uptime displayed on the website. Then, once admin access is obtained through the spoofed JWT, arbitrary path traversal must be achieved by requesting a file that bypasses the traversal filter. This is done by including an absolute path in the `filename` parameter (`os.join()` will use the full path if one is provided for some reason). Then, the flag is located in an unknown directory, but can be accessed through `/proc/self/cwd/flag.txt`. 

This process is automated in `solve.py`.

**Flag** - `byuctf{expl01t_chains_involve_multiple_exploits_in_a_row}`

## Hosting
This challenge should be a Docker container that runs the Flask server `server.py` on port 40000. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
bash start_docker.sh
```

To stop the challenge:
```bash
docker compose down
```