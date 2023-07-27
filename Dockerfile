FROM python:3.8.10

USER root

RUN mkdir /app
WORKDIR /app

COPY ./ /app/

RUN python -m venv venv
RUN /app/venv/bin/activate

RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENV PYTHONUNBUFFERED=1

CMD [ "python", "/app/main.py" ]
