from collections.abc import AsyncGenerator

from sqlalchemy import Column, String, Text, DateTime, Integer

# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

# from fastapi_users.db import SQLAlchemyUserDatabase, SQLAlchemyBaseUserTableUUID

DATABASE = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True)
    quote = Column(Text, nullable=False)
    author = Column(String)
    notes = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    # user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
