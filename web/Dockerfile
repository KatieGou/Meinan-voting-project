FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY web .

COPY config.py .env ./

EXPOSE 5000

CMD ["python3", "app.py"]