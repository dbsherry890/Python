from sqlmodel import SQLModel, Field, Relationship

# from datetime import datetime


class Make(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    country: str
    founded: int
    models: list["Model"] = Relationship(back_populates="make")


class Model(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1)
    body_style: str
    year_start: int = Field(ge=1900)
    year_end: int | None = None

    make_id: int = Field(foreign_key="make.id")
    make: Make = Relationship(back_populates="models")


# class CarModelUpdate(CarModelBase):
#     name: str | None = None
#     body_style: str | None = None
#     year_start: str | None = None
#     year_end: str | None = None
