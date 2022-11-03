# spefic the parent image
FROM node:carbon
# change working directory inside the image
WORKDIR /usr/src/app
# move files into the current working directory, so that we can install dependencies using npm install
COPY package*.json ./
RUN npm install
# copy all code in the currently directory inside the image
COPY . .
EXPOSE 3000
CMD [ "npm", "start" ]