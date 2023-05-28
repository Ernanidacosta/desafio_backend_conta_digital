FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000"]


