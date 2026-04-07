FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
