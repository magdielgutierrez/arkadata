#Use python 3.10
FROM python:3.10.1

# Copy file requirements.txt
COPY ./requirements.txt /app/requirements.txt

# Create directory
WORKDIR /app

# Excecute udpate pip 
RUN pip install --upgrade pip

# Excecute install requirements in requirements.txt 
RUN pip install -r requirements.txt

# Copy the app folder
COPY . /app

# Define port 5000
EXPOSE 5000

# Delete file requirements.txt
RUN rm  /app/requirements.txt

# Execute app.py
ENTRYPOINT ["python3" ]
CMD ["app.py"]
