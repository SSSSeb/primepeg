from ubuntu:latest

RUN apt -y update && apt -y upgrade && apt -y install python3 python3-gmpy2 exiftool imagemagick emacs-nox
RUN mkdir -p /home/seb/HP_data/
COPY *.jpg /home/seb/HP_data/
COPY gmpython.py .
ENTRYPOINT sleep infinity
