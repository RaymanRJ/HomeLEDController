FROM python:3.8-slim-buster

COPY ./app ./app

WORKDIR ./app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "Main.py" ]
