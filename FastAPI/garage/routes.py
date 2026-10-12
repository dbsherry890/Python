from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return "yuh bish"


@router.get("/list/{id}")
def listid(id: int):
    return f"you typed id: {id}"
