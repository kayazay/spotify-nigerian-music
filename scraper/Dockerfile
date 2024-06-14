FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

RUN pip install --upgrade -r req.txt

CMD bash
#python3 script.py

#sample of env.cfg
#[spotipy.client]
#id = secret = uri = https://open.spotify.com/playlist/37i9dQZF1DWUf3j9Rl2IUG?si=5f6b3e70ca0145fb

