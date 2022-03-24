from ubuntu:latest

ENV http_proxy=http://web-proxy.gre.hpecorp.net:8080
ENV https_proxy=http://web-proxy.gre.hpecorp.net:8080

RUN apt -y update && apt -y upgrade
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt -y install exiftool imagemagick emacs-nox
RUN apt -y install python3 python3-gmpy2 
RUN mkdir -p /home/seb/HP_data/
COPY *.jpg /home/seb/HP_data/
COPY gmpython.py .
ENTRYPOINT sleep infinity
