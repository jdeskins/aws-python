FROM python:3.6-alpine


RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip awscli boto3

RUN mkdir /project

WORKDIR /project

ADD scripts /project/scripts

ENV PATH=/project/scripts:$PATH

CMD "/bin/bash"
