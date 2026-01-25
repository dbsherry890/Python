# SQLModel

## Summary
Basically SQLAlchemy and Pydantic combined and simplified: “Pydantic-first SQLAlchemy”
Designed by FastAPI author
Considered "lighter" than SQLAlchemy 


```from sqlmodel import SQLModel, Field

# defines table structure, validates data, serializes this to JSON
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
```

