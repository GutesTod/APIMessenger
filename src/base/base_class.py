from typing import Generic, Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from src.config.settings import Base
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy import update, delete


ModelType = TypeVar("ModelType", bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self.table = model
        self.db_session = db_session

    async def get(self):
        async with self.db_session as session:
            query = await session.execute(
                select(self.table).order_by(-self.table.id.desc())
            )
            return query.scalars().all()

    async def get_one(self, id):
        async with self.db_session as session:
            id_item = await session.execute(
                select(self.table).filter(self.table.id == id)
            )
            id_item = id_item.scalar()
        if not id_item:
            raise HTTPException(status_code=404, detail="Page is not found")
        return id_item

    async def create(self, data):
        async with self.db_session as session:
            item = self.table(**data.dict())
            session.add(item)
            await session.commit()
        return item

    async def update(self, data):
        async with self.db_session as session:
            await session.execute(
                update(self.table),
                [data.dict()],
            )
            await session.commit()
        return await self.get_one(data.id)

    async def delete(self, id):
        async with self.db_session as session:
            await session.execute(
                delete(self.table).filter(self.table.id == id)
            )
            await session.commit()
        return None