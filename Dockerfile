FROM node:16

#https://nodejs.org/en/docs/guides/nodejs-docker-webapp/



# Create app directory

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
#COPY . .
COPY . /usr/src/app

EXPOSE 8080

#CMD [ "node", "server.js" ]
#CMD [ "npm", "start" ]
CMD [ "npm", "run", "serve" ]

# BUILD
#docker build . -t ait-front_end/node-web-app

#RUN 
#docker run -p 49160:8080 -d ait-front_end/node-web-app
#Browser: http://localhost:49160/


# Enter the container
# docker exec -it <container id> /bin/bash
