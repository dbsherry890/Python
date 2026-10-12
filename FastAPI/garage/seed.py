from sqlmodel import Session
from models import Model, Make
from db import engine


def create_cars():
    with Session(engine) as session:
        bmw = Make(name="BMW", country="Germany", founded=1901)
        session.add(bmw)
        session.commit()
        session.refresh(bmw)

        m2 = Model(name="M2", body_style="coupe", year_start=2023, make_id=bmw)
        x3 = Model(name="X3", body_style="SUV", year_start=2012, make_id=1)

        session.add(m2)
        session.add(x3)

        session.commit()

        session.refresh(m2)
        session.refresh(x3)
