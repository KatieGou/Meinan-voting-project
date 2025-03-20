FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY result .

EXPOSE 5001

CMD ["python3", "app.py"]