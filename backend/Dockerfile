FROM python:3.12@sha256:491834927515f4e3f360775d862e342718e27c1f9d6c1c010d19f3f4a3861234

WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
