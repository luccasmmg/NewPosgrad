FROM node:12

ADD package.json /package.json

ENV NODE_PATH=/node_modules
ENV PATH=$PATH:/node_modules/.bin
RUN yarn

WORKDIR /app
ADD . /app

EXPOSE 8000
EXPOSE 35729

RUN yarn build
ENTRYPOINT ["/bin/bash", "/app/run.sh"]
CMD ["serve"]
