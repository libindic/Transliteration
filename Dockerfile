# Use this file to build a docker image of libindic-transliteration
#
#    sudo docker build -t libindic_transliteration .
#
# Then open a bash session in docker with:
#
#    sudo docker run -it libindic_transliteration /bin/bash
#
# You can then use libindic-transliteration within docker.


# Use an official Ubuntu as a parent image
FROM ubuntu:18.04

# install dependencies
RUN apt-get update 
# RUN apt-get upgrade -y 
RUN apt-get install -y \
        git \
        nano \
        python3 \
        python3-pip \
        locales
RUN apt-get clean

# Set the locale
# https://stackoverflow.com/questions/28405902/how-to-set-the-locale-inside-a-debian-ubuntu-docker-container
# source - http://jaredmarkell.com/docker-and-locales/
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
RUN locale-gen "en_US.UTF-8"

# libindic transliteration needs a few things before it works
RUN git clone https://github.com/nitinthewiz/normalizer.git && \
	cd normalizer && \
	python3 setup.py install

RUN pip3 install libindic-utils

# install libindic transliteration and run the tests
RUN git clone https://github.com/nitinthewiz/Transliteration.git /Transliteration && \
    cd /Transliteration && \
    python3 setup.py install

WORKDIR /Transliteration

