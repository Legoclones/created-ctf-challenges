FROM debian:bookworm-slim

# dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y openssh-server python3 sudo
RUN rm -rf /var/lib/apt/lists/*

# setup unpriv user with `sudo ls` permission
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf
RUN echo "ctf:e0834310e54090a4" | chpasswd
RUN echo 'ctf ALL=(ALL) /usr/bin/ls' > /etc/sudoers.d/ctf

# setup ssh
RUN mkdir /run/sshd
RUN ssh-keygen -A
RUN rm /usr/bin/kill /usr/bin/pkill
RUN echo 'MaxSessions 50' >> /etc/ssh/sshd_config
RUN echo 'MaxStartups 50:30:70' >> /etc/ssh/sshd_config

# copy files
COPY start.sh /start.sh
RUN mkdir /scripts
COPY processes.py /processes.py
RUN python3 /processes.py
RUN rm /processes.py
RUN chmod -R 700 /start.sh /scripts

# run
CMD ["bash", "/start.sh"]
EXPOSE 22