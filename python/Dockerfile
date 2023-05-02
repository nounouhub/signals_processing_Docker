# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

RUN pip install mysql-connector-python

WORKDIR /usr/app/src
COPY signalsApi.py ./
# COPY signalsProcessing.py ./
# COPY persistence.py ./
