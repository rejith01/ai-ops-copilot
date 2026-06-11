from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)

from src.infrastructure.config.settings import settings

DATABASE_URL = settings.database_url.replace(
    "postgresql://",
    "postgresql+asyncpg://",
)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)