from ubuntu:latest

RUN apt -y update && apt -y upgrade
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt -y install exiftool imagemagick emacs-nox
RUN apt -y install python3 python3-gmpy2 python3-sympy
RUN mkdir -p /home/seb/HP_data/
COPY *.jpg /home/seb/HP_data/
COPY gmpython.py .
COPY test_prime.py .
ENTRYPOINT sleep infinity
