from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str

    class Config:
        env_file = "./env/.env"
        env_file_encoding = "utf-8"


settings = Settings()


engine = create_async_engine(settings.db_url, echo=True)

# Создаем асинхронный sessionmaker
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_session():
    async with SessionLocal() as db:
        try:
            yield db
        except Exception:
            await db.rollback()
            raise
        else:
            await db.commit()


class Base(DeclarativeBase):
    pass