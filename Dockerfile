FROM python:3.8.10

USER root
RUN mkdir /app

COPY ./ /app/

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENV PYTHONUNBUFFERED=1

CMD [ "python", "/app/main.py" ]
