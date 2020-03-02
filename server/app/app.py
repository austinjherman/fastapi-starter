from . import models
from app.database import engine

from fastapi import FastAPI
from . import routes


def create_app():
    models.Base.metadata.create_all(bind=engine)
    app = FastAPI()
    app.include_router(routes.router)
    return app
