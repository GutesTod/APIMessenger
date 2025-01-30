from fastapi import APIRouter, Depends

from .schemas import DialogCreate, DialogResponse
from .service import get_dialog_service, DialogService

dialog_router = APIRouter(prefix="/dialog", tags=['Диалоги'])

@dialog_router.post("/", response_model=DialogResponse)
async def create_dialog(
    data: DialogCreate,
    service: DialogService = Depends(get_dialog_service)
):
    return service.create(data=data)