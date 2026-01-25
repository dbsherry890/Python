# duckdb_example.py
from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session


# ----------------
# MODELS
# ----------------
class Base(DeclarativeBase):
    """Base class for all models."""
    pass


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    fname: Mapped[str] = mapped_column(String(32), nullable=False)
    lname: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)

    notes: Mapped[List["Note"]] = relationship(
        back_populates="person", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Person {self.fname} {self.lname}>"


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow)
    person_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("persons.id"), nullable=False)

    person: Mapped[Person] = relationship(back_populates="notes")

    def __repr__(self) -> str:
        return f"<Note {self.id} for Person {self.person_id}>"


# ----------------
# DATABASE SETUP
# ----------------
# ✅ Use a persistent file OR in-memory — pick one.
# DuckDB URI format: duckdb:///file_name.duckdb   (3 slashes)
engine = create_engine("duckdb:///example.duckdb", echo=True)

# Create tables
Base.metadata.create_all(engine)

# ----------------
# DATA INSERTION
# ----------------
with Session(engine) as session:
    # Create a Person
    alice = Person(fname="Alice", lname="Smith")
    session.add(alice)
    session.commit()

    # Add a note
    note1 = Note(content="Alice's first note", person=alice)
    session.add(note1)
    session.commit()

# ----------------
# QUERY EXAMPLE
# ----------------
with Session(engine) as session:
    people = session.query(Person).all()
    for p in people:
        print(p, p.notes)
