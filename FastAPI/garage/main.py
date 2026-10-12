from seed import create_cars
from db import init_db, discard_db, engine
from sqlmodel import Session, select
from models import Make, Model


def main():
    discard_db()
    init_db()
    create_cars()  # seed

    with Session(engine) as session:
        for make in get_makes(session):
            print(make)
        # m2 = session.get(Model, 1)
        # if m2 is not None:
        #     m2.year_end = 2027


def get_models(session: Session) -> list[Model]:
    models = list(session.exec(select(Model)).all())
    return models


def get_makes(session: Session) -> list[Make]:
    makes = list(session.exec(select(Make)).all())
    return makes


if __name__ == "__main__":
    main()


# from fastapi import FastAPI
# from routes import router
#
#
# def lifespan(app: FastAPI):
#     discard_db()
#     init_db()
#     create_cars()
#     yield
#
#
# app = FastAPI(lifespan=lifespan, debug=True)
# app.include_router(router)
