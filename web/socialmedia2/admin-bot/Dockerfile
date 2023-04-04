FROM node:12.18.1
 
WORKDIR /bot
 
COPY ./bot /bot
RUN npm install
EXPOSE 1337

CMD [ "node", "bot.js" ]
