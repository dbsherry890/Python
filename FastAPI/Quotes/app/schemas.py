from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class QuoteRead(BaseModel):
    id: int
    author: str
    quote: str
    created_at: datetime


class QuoteCreate(BaseModel):
    quote: str
    author: str
    notes: Optional[str] = None


class QuoteModify(BaseModel):
    quote_id: int
    quote: str
    old_item: str
    new_item: str
