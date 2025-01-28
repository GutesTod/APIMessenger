from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str

    class Config:
        env_file = "./env/.env"
        env_file_encoding = "utf-8"


settings = Settings()


engine = create_engine(settings.db_url)


async def get_session():
    session = sessionmaker(engine, expire_on_commit=False)
    return session


class Base(DeclarativeBase):
    pass