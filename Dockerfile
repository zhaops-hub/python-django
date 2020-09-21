FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1

RUN echo 'nameserver 114.114.114.114' >> /etc/resolv.conf

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
