import os
from fastapi import FastAPI
from app.database import FastDB


db = FastDB()


def create_app():
    db.init_db(os.environ.get('DATABASE_URL_DEV'))
    app = FastAPI()
    return app


def create_test_app():
    app = FastAPI()
    return app
