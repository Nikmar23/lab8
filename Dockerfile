FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install psycopg2-binary
CMD ["python", "script.py"]