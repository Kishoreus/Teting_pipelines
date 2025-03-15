FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r -v requierments.txt

ENTRYPOINT ["python"]

cmd ["app.py"]
