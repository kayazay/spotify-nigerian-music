FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY scraper/. env.cfg ./

RUN pip install --upgrade -r req.txt

CMD python3 script.py
