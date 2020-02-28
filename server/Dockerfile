FROM python:3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/server
COPY . .

RUN pip install -r ./requirements.txt --trusted-host=files.pythonhosted.org
RUN chmod +x ./start.sh

EXPOSE 80