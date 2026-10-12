# from fastapi import Depends
from sqlmodel import create_engine, SQLModel, Session

url = "sqlite:///./garage.db"
engine = create_engine(url, connect_args={"check_same_thread": False})  # , echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def discard_db():
    SQLModel.metadata.drop_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


# SessionDep = Annotated[Session, Depends(get_session)]
