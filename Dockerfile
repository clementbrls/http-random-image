FROM python:3.11-slim

RUN pip install flask gunicorn

WORKDIR /app
COPY app.py .

EXPOSE 8080

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]
