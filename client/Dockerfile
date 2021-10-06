FROM node:alpine

RUN mkdir /app

WORKDIR /app

COPY package.json yarn.lock ./

COPY ./ ./

RUN yarn install

EXPOSE 3000

CMD ["yarn", "dev"]

# CMD ["npm", "run", "dev"]

# prod CMD ["yarn", "start"]