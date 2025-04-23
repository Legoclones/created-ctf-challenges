FROM python:3
ARG directory=/in_prod_this_is_random

# dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN rm -rf /var/lib/apt/lists/*
RUN pip3 install flask PyJWT

# setup unpriv user
RUN mkdir ${directory}
RUN useradd -M -d ${directory} ctf

# copy files
COPY server.py ${directory}/server.py
COPY flag.txt ${directory}/flag.txt
RUN mkdir -p ${directory}/files
RUN for i in {1..5}; do (echo $(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1) > ${directory}/files/$(cat /dev/urandom | tr -dc a-f0-9 | fold -w32 | head -n1)); done

# file perms
RUN chown -R root:ctf ${directory} 
RUN chmod -R 750 ${directory}

# run
USER ctf
WORKDIR ${directory}
CMD ["python3", "server.py"]
EXPOSE 1337