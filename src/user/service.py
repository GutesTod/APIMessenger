from fastapi import Depends

from src.base.base_class import BaseService
from src.config.settings import get_session

from .model import Users

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete

class UserService(BaseService[Users]):
    def __init__(self, db_session: AsyncSession):
        super(UserService, self).__init__(Users, db_session)
        
    async def get(self, username: str, password: str):
        async with self.db_session as session:
            query = await session.execute(
                select(self.table).filter(
                    self.table.username == username,
                    self.table.password == password
                )
            )
            return query.scalar_one_or_none()
        
    
def get_user_service(
    db_session: AsyncSession = Depends(get_session)
):
    return UserService(db_session=db_session)