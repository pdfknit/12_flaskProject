FROM python:3.9.1-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY . .
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
