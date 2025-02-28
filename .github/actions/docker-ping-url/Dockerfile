FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN python -V
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN ls -al /app

CMD env && python /app/main.py
