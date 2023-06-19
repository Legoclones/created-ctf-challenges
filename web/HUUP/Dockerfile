FROM python:3

# dependencies
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# create ctf user
RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

# copy files
COPY start.sh /ctf/start.sh
COPY server.py /ctf/server.py
COPY flag.txt /ctf/flag.txt
COPY endpoints.txt /ctf/endpoints.txt
COPY udp_server.py /ctf/udp_server.py

# set permissions
RUN chown -R root:ctf /ctf 
RUN chmod -R 750 /ctf

# install python dependencies
RUN pip3 install flask

CMD ["/ctf/start.sh"]

EXPOSE 40000/udp