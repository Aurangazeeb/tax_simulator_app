FROM python:3.8

WORKDIR /tax_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/calculator_app.py"]