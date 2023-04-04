FROM ubuntu:latest

# update and install dependencies
RUN apt update && apt upgrade -y && apt install openssh-server locales locales-all ufw -y

# add user for players to log in as (NO sudo access)
RUN useradd -rm -d /home/byuctf -s /bin/bash -u 1000 byuctf
RUN  echo 'byuctf:CosmoCougar!' | chpasswd

# run startup script to add in files and directories
COPY startup.sh /home/byuctf/startup.sh
RUN cd /home/byuctf && bash /home/byuctf/startup.sh
RUN rm /home/byuctf/startup.sh

# change owner to root so files can't be added (including .bash_history), only read
RUN chown -R root:root /home/byuctf
RUN chown -R root:root /tmp

# delete binaries that you don't want them to use (mainly ones with SUID bit set)
RUN rm -f /usr/bin/passwd
RUN rm -f /usr/bin/chsh
RUN rm -f /usr/bin/mount
RUN rm -f /usr/bin/su
RUN rm -f /usr/bin/umount

# enable UTF-8 support so Unicode characters can be seen properly
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# run SSH server
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]