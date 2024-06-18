FROM python:3.9-slim

WORKDIR /kaggle
COPY kaggle.json /root/.kaggle/
COPY *.csv *.md dataset-metadata.json ./

RUN pip3 install kaggle==1.6.14

CMD kaggle datasets version -m "weekly upload of spotify music"
