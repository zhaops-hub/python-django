FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN echo 'nameserver 114.114.114.114' >> /etc/resolv.conf

RUN mkdir /code
WORKDIR /code


RUN pip install pip -U

RUN mkdir -p ~/.pip

# pip设置国内源
ADD ./pip.conf /code/
RUN mv /code/pip.conf ~/.pip

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
