#Use python 3.10
FROM python:3.10.1

# Copy file requirements.txt
COPY ./requirements.txt /app/requirements.txt

# Create directory
WORKDIR /app

# Execute udpate pip 
RUN pip install --upgrade pip

# Execute apk MySQL password autentication
RUN pip install cryptography

# Execute install requirements in requirements.txt 
RUN pip install -r requirements.txt

# Copy the app folder
COPY .  /app
COPY /src /app/

# Define port 8000
EXPOSE 8000

# Delete file requirements.txt
RUN rm  /app/requirements.txt

# Execute app.py
ENTRYPOINT ["python3" ]
CMD ["app.py"]
