from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Note, Person

# Connect to SQLite
engine = create_engine("sqlite:///people.db", echo=False, future=True)
session = Session(engine)

print("✅ Connected to SQLite DB")
print("Models loaded: Person, Note")
print("Example query: session.scalars(select(Person)).all()")

import code

code.interact(local=locals())
