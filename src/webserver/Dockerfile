FROM python:3.8-slim-buster

COPY ./app .

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt


ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD ["app/Main.py"]
