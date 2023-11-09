FROM python:3.8-slim-buster
RUN apt-get update
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN --mount=type=secret,id=env cat /run/secrets/env > /app/secret
COPY ./app.py app.py
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]