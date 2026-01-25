from fastapi import FastAPI, HTTPException, Depends
from app.schemas import *
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from app.db import create_db_and_tables, get_async_session, Quote
from sqlalchemy import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

tags_metadata = [
    {
        "name": "Main section",
        "description": "Add description for main section",
    },
    {
        "name": "Other section",
        "description": "Add description for other section",
    },
]

app = FastAPI(title="Qutoes API",
              openapi_tags=tags_metadata, lifespan=lifespan)

mem_db = [
    {
        "id": 1,
        "author": "Nelson Mandela",
        "quote": "It always seems impossible until it’s done."
    },
    {
        "id": 2,
        "author": "Walt Disney",
        "quote": "The way to get started is to quit talking and begin doing."
    },
    {
        "id": 3,
        "author": "Confucius",
        "quote": "It does not matter how slowly you go as long as you do not stop."
    },
    {
        "id": 4,
        "author": "Eleanor Roosevelt",
        "quote": "The future belongs to those who believe in the beauty of their dreams."
    },
    {
        "id": 5,
        "author": "Steve Jobs",
        "quote": "Stay hungry, stay foolish."
    },
    {
        "id": 6,
        "author": "Vince Lombardi",
        "quote": "Winners never quit and quitters never win."
    },
    {
        "id": 7,
        "author": "Albert Einstein",
        "quote": "In the middle of every difficulty lies opportunity."
    },
    {
        "id": 8,
        "author": "Henry Ford",
        "quote": "Whether you think you can or think you can’t, you’re right."
    },
    {
        "id": 9,
        "author": "Maya Angelou",
        "quote": "You will face many defeats in life, but never let yourself be defeated."
    },
    {
        "id": 10,
        "author": "Theodore Roosevelt",
        "quote": "Believe you can and you’re halfway there."
    }
]


@app.get("/quotes")
async def read_quotes(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Quote))
    quotes = [row[0] for row in result.all()]

    quotes_data = []
    for quote in quotes:
        quotes_data.append({
            "id": str(quote.id),
            "quote": quote.quote,
            "author": quote.author,
            "notes": quote.notes,
            "created_at": quote.created_at
        })

    return {"quotes": quotes_data}


@app.get("/quotes/{quote_id}", response_model=QuoteRead)
async def get_quote(
        quote_id: int,
        session: AsyncSession = Depends(get_async_session)):

    # Look up the existing quote by ID
    result = await session.execute(select(Quote).where(Quote.id == quote_id))
    db_quote = result.scalar_one_or_none()

    if db_quote is None:
        raise HTTPException(status_code=404, detail="Quote not found")

    return db_quote


@app.post("/addquote")
async def add(
    quote: QuoteCreate,
    session: AsyncSession = Depends(get_async_session)
):
    db_quote = Quote(
        quote=quote.quote,
        author=quote.author,
        notes=quote.notes
    )
    session.add(db_quote)
    await session.commit()
    await session.refresh(db_quote)
    return {
        "id": db_quote.id,
        "quote": db_quote.quote,
        "author": db_quote.author,
        "notes": db_quote.notes
    }
