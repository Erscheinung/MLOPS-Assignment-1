FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Using Port 80 here
EXPOSE 80

CMD ["python", "src/main.py"]