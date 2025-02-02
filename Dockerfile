FROM mcr.microsoft.com/devcontainers/python:3.11

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip install --upgrade pip && \
pip install autopep8 pylint black flake8 bandit && \
pip install fastapi uvicorn && \
pip install pymongo 