FROM python:3.9-slim

WORKDIR /kaggle
COPY kaggle.json /root/.kaggle/
COPY *.csv *.md dataset-metadata.json ./

RUN pip3 install kaggle==1.6.14

ENTRYPOINT ["kaggle", "datasets", "version", "-q", "-d", "-m", "weekly upload of spotify music"]
