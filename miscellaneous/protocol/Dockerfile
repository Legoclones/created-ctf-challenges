FROM python:3 AS app

# dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN rm -rf /var/lib/apt/lists/*

# import into jail
FROM pwn.red/jail
COPY --from=app / /srv

# copy files over
COPY server.py /srv/app/run

# setup jail
ENV JAIL_TIME=30 JAIL_MEM=20M JAIL_CONNS_PER_IP=10