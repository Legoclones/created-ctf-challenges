#!/bin/bash

# run server as ctf in the background
su ctf -c "python3 /ctf/server.py" &

# run udp server in loop to restart it if it crashes
while true; do (python3 /ctf/udp_server.py); done