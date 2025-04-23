# Reboot
Description:
```markdown
We found a command injection..... but you have to reboot the router to activate it...

`nc reboot.chal.cyberjousting.com 1358`

[reboot.zip]
```

## Writeup
Attempts to establish a reverse shell won't work because outbound Internet access is disabled, same with reading commands from an external webserver. There's also a 30 character limit, and 2 of those must be `;` on either side of the command. They do, however, have `/dev/shm/` available to write to files. The easiest solution I've found is the following:

```bash
;find /o* -type f>/dev/shm/a;
;cat $(cat /dev/shm/a);
```

**Flag** - `byuctf{expl0iting_th1s_r3al_w0rld_w4s_s000_ann0ying}`

## Hosting
This challenge should be a Docker container that runs the script `server.py` on port 40003 each time a user connects. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```

It should have a firewall rule that disallows ALL outbound internet traffic on the host.