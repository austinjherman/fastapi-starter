from fastapi import FastAPI
from app import routes


def create_app():
    app = FastAPI()
    app.include_router(routes.router)
    return app
