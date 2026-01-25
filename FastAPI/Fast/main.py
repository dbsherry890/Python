from fastapi import FastAPI, APIRouter, Request
from pydantic import BaseModel
from uvicorn import run
from enum import Enum
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.config import settings
from db.base import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    create_tables()
    return app


app = start_application()


@app.get("/")
def home():
    return {"message": "yuh world"}


app()
