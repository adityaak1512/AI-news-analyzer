<<<<<<< HEAD
FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

=======
FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

>>>>>>> e1e754f (Initial commit)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]