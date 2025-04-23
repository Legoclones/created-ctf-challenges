FROM ubuntu:23.04

# install dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y xinetd libcapstone4 libglib2.0-dev
RUN rm -rf /var/lib/apt/lists/*

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
RUN echo "Connection blocked" > /etc/banner_fail
COPY src/ctf.xinetd /etc/xinetd.d/ctf
COPY src/lib /lib
COPY src/app /ctf
COPY pwd.txt /ctf
COPY flag.txt /ctf

# file perms
RUN chmod -R 750 /ctf
RUN chown -R root:ctf /ctf

# run
CMD ["/usr/sbin/xinetd", "-dontfork"]
EXPOSE 40000