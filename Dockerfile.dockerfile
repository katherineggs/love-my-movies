FROM python:3-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "movie.py" ]

EXPOSE 5000