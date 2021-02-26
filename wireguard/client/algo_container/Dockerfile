FROM library/python:3.7-alpine

RUN apk update
RUN apk upgrade
RUN apk add bash
RUN apk add wireguard-tools

ADD entry.sh .
ADD algo.py .

ENTRYPOINT ["bash", "entry.sh"]

CMD ["python", "algo.py"]
