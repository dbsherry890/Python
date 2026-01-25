from datetime import datetime
from typing import List
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config import db


class Person(db.Model):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True)
    fname: Mapped[str] = mapped_column(String(32), nullable=False)
    lname: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)

    notes: Mapped[List["Note"]] = relationship(
        back_populates="person", cascade="all, delete-orphan"
    )


class Note(db.Model):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("persons.id"), nullable=False
    )

    person: Mapped["Person"] = relationship(back_populates="notes")
