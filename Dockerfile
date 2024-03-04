FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DEBUG FALSE
ENV PYTHONUNBUFFERED TRUE

ENV SMTP_SERVER 'smtp.gmail.com'
ENV PORT 587

ENV SENDER_EMAIL 'foo@bar.com'
ENV OWNER_EMAIL 'bar@foo.com'
ENV PASSWORD 'PASSWORD'

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]