FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN echo 'nameserver 114.114.114.114' >> /etc/resolv.conf

RUN mkdir /code
WORKDIR /code


# 安装依赖库
RUN rm -rf /etc/apt/sources.list
ADD ./sources.list /etc/apt/
RUN cat /etc/apt/sources.list
RUN apt update
RUN apt install -y libgl1-mesa-dev


# pip设置国内源
RUN pip install pip -U
RUN mkdir -p ~/.pip
ADD ./pip.conf /code/
RUN mv /code/pip.conf ~/.pip

ADD requirements.txt /code/
RUN pip install -r requirements.txt


ADD . /code/
