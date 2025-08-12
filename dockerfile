FROM python:3.11-slim

WORKDIR /server

COPY requirements.txt /server/

RUN pip install --no-cache-dir -r requirements.txt

COPY counter-service.py /server/

EXPOSE 80

CMD ["python", "counter-service.py"]
