# Netstat
Description:
```markdown
Which Python script is listening on TCP port 9876? Password is `e0834310e54090a4`.

Flag format - `byuctf{scriptname.py}`

`ssh ctf@netstat.chal.cyberjousting.com -p 1353`
```

Maximum 5 ATTEMPTS

## Writeup
The goal here is to see what processes have which ports open without the `netstat` or other useful binary + without the ability to see the contents of the custom Python scripts. When you SSH on, you have `sudo ls` access, which is necessary for the solve. What you do is look in `/proc/self/tcp` for the inode of the socket listening on port 9876 (`0x2694`), then look inside `/proc/<pid>/fd` to see which file descriptor symlinks to a socket with that inode. 

A quick solution is shown below:

```bash
sudo ls -l /proc/*/fd 2>/dev/null | grep -B 6 $(cat /proc/net/tcp | grep 2694 | awk '{print $10}') | grep /proc
ps -aux | grep ' 68 ' | awk '{print $12}' # assuming the pid from above command is 68
```

**Flag** - `byuctf{5065fc12633a9f1fd28f0b9d27467537.py}`

## Hosting
This challenge should be a Docker container that runs SSH on port 22. All the proper files are included in here. The command to build and run the docker container is (when located inside of this directory):

```bash
docker compose up -d
```

To stop the challenge:
```bash
docker compose down
```