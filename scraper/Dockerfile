FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY *.txt .
RUN pip install --upgrade -r requirements.txt


WORKDIR /app
COPY . .

CMD ["python3", "script.py"]
