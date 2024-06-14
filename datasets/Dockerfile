FROM python:3.9-slim

COPY kaggle.json /root/.kaggle/

WORKDIR /kaggle
COPY *.csv *.md dataset-metadata.json ./

RUN pip3 install kaggle

CMD bash
#kaggle datasets version -m "weekly upload of spotify music"


#sample of kaggle.json
#{"username": "", "key": ""}
