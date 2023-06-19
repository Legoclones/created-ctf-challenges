FROM ubuntu

# update and install xinetd
RUN apt-get update && apt-get install -y xinetd
RUN rm -rf /var/lib/apt/lists/*

# create ctf user
RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

# copy files
RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY vfs1 /ctf/vfs1
COPY flag.txt /ctf/flag.txt
COPY start.sh /ctf/start.sh

# set permissions
RUN chown -R root:ctf /ctf
RUN chmod -R 750 /ctf

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 40000