FROM python:3.9-slim

ENV KAGGLE_USERNAME=kemdudebobo
ENV KAGGLE_KEY=65e7569fa0af192a09af81129058faf3

WORKDIR /kaggle
COPY *.csv *.json .

RUN pip3 install kaggle

CMD kaggle datasets version -m "Weekly upload of spotify music"
