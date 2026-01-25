import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List


class Gift(BaseModel):
    name: str


class Gifts(BaseModel):
    gifts: List[Gift]


app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

memory_db = {"gifts": []}


@app.get("/gifts", response_model=Gifts)
def get_gifts():
    return Gifts(gifts=memory_db["gifts"])


@app.post("/gifts", response_model=Gift)
def add_gift(gift: Gift):
    memory_db["gifts"].append(gift)
    return gift


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
