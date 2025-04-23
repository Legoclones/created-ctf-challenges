FROM python:3

# dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install flask

# setup unpriv user
RUN mkdir /ctf
RUN useradd -M -d /ctf ctf

# copy files
COPY server.py /ctf/server.py
COPY templates /ctf/templates
RUN mkdir -p /ctf/uploads/
COPY flag.txt /flag.txt
RUN mv /flag.txt /flag_$(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1)

# file perms
RUN chown -R root:ctf /ctf 
RUN chmod -R 750 /ctf
RUN chown ctf:ctf /ctf/uploads/

# run
USER ctf
WORKDIR /ctf
CMD ["python3", "server.py"]
EXPOSE 1337