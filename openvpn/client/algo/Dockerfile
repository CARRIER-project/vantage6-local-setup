FROM library/python:3.7-alpine

RUN apk update
RUN apk upgrade
RUN apk add bash

ADD algo.sh .

CMD ["bash", "algo.sh"]
