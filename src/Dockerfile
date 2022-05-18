
FROM python:3.10.1

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3" ]
CMD ["app.py"]
