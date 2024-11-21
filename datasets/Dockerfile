FROM python:3.9-slim

WORKDIR /kaggle
COPY kaggle.json /root/.kaggle/
RUN chmod 600 /root/.kaggle/kaggle.json

COPY *.csv *.md dataset-metadata.json ./

RUN pip3 install kaggle==1.6.17

ENTRYPOINT ["kaggle", "datasets", "version", "-q", "-d", "-m", "weekly upload of spotify music"]
