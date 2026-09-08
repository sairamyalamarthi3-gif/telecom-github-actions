FROM python:3.12-slim

WORKDIR /app

COPY availability.py .
COPY app.py .

CMD ["python", "app.py"]
