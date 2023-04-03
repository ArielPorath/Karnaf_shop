FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY karnaf_shop /app/karnaf_shop

ENV PYTHONPATH="/app"
ENV REDIS_PORT=6379

CMD ["uvicorn", "karnaf_shop.main:app", "--host", "0.0.0.0", "--port", "8081"]