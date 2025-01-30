from fastapi import Depends

from src.base.base_class import BaseService
from src.config.settings import get_session

from .model import Message

from sqlalchemy.ext.asyncio import AsyncSession

class MessageService(BaseService[Message]):
    def __init__(self, db_session: AsyncSession):
        super(MessageService, self).__init__(Message, db_session)
        
    
        
def get_message_service(
    db_session: AsyncSession = Depends(get_session)
):
    return MessageService(db_session=db_session)