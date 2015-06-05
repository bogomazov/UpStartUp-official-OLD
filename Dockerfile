FROM ubuntu:14.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python python-pip

RUN apt-get install postgis -y
RUN apt-get install libgeos-3.4.2

RUN apt-get -y install wget zip gcc
RUN wget http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
RUN tar xjf geos-3.4.2.tar.bz2; cd geos-3.4.2; ./configure; make; make install

FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /upstartup
WORKDIR /upstartup
ADD requirements.txt /upstartup/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /upstartup/


