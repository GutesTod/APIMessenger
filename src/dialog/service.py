from fastapi import Depends

from src.base.base_class import BaseService
from src.config.settings import get_session

from .model import Dialog

from sqlalchemy.ext.asyncio import AsyncSession

class DialogService(BaseService[Dialog]):
    def __init__(self, db_session):
        super(self, DialogService).__init__(Dialog, db_session)
        
def get_dialog_service(
    session: AsyncSession = Depends(get_session)
):
    return DialogService(session)