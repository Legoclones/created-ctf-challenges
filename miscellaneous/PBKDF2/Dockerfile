FROM node:19.7.0-bullseye-slim

# setup web server
WORKDIR /app
COPY flag.txt flag.txt
COPY server.js server.js
COPY package.json package.json

RUN npm install

# install 7zip and make zip file
RUN apt-get update && apt-get install -y p7zip-full
RUN 7z a flag.zip flag.txt -mem=AES256 '-pisnt-byuctf-one-of-your-most-favorite-ctfs-even-though-this-is-only-our-second-year-3HF4z'
RUN rm flag.txt

# create and use unprivileged user
RUN useradd -M -d /app ctf
RUN chown -R root:ctf /app && chmod -R 750 /app

USER ctf

EXPOSE 8080

CMD ["node", "server.js"]