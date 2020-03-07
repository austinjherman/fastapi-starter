#!/bin/sh

## For development
uvicorn main:app --reload --host 0.0.0.0 --port 80

## For Production
# gunicorn -b 0.0.0.0:80 main:app -w 4 -k uvicorn.workers.UvicornWorker --reload