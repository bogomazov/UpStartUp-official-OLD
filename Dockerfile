RUN apt-get install geos

FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /upstartup
WORKDIR /upstartup
ADD requirements.txt /upstartup/
RUN pip install -r requirements.txt
ADD . /upstartup/

