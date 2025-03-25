FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY worker .

COPY config.py .env ./

CMD ["python3", "worker.py"]