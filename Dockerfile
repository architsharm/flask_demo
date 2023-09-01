FROM python:3.8-slim-buster
WORKDIR /flask-docker
COPY requirements.txt requirements.txt
COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]