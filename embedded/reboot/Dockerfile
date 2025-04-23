FROM debian:bullseye-slim

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3 xinetd
RUN rm -rf /var/lib/apt/lists/*

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY start.sh /ctf
COPY server.py /ctf
COPY flag.txt /ctf
COPY xinetd.sh /ctf/xinetd.sh
COPY clean.sh /ctf/clean.sh

RUN mkdir -p /ohno/i/hope/this/isnt/too/long/is/this/messing/you/up/lol/arent/ctfs/so/much/fun/
RUN mv /ctf/flag.txt /ohno/i/hope/this/isnt/too/long/is/this/messing/you/up/lol/arent/ctfs/so/much/fun/$(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1)

# file perms
RUN chmod -R 750 /ctf
RUN chown -R root:ctf /ctf

# run
CMD ["bash", "/ctf/start.sh"]
EXPOSE 40000