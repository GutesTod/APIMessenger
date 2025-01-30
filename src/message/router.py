from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect

from .schemas import MessageCreate
from .service import MessageService, get_message_service
from .utils import ConnectionManager
from src.dialog.service import DialogService, get_dialog_service

message_router = APIRouter(prefix="/message")

manager = ConnectionManager()
    
@message_router.websocket("/ws/{user_id}")
async def websocket_message(
    websocket: WebSocket,
    data: MessageCreate,
    message_service: MessageService = Depends(get_message_service),
    dialog_service: DialogService = Depends(get_dialog_service)
):
    await manager.connect(websocket, id)
    try:
        while True:
            data = await websocket.receive_text()
            # Handle incoming message
            await message_service.create(data=data)

            dialog = await dialog_service.get_one(data.dialog_id)
            other_user_id = dialog.user1_id if dialog.user1_id != data.sender_id else dialog.user2_id
            await manager.send_message(data.content, receiver_id=other_user_id)
    except WebSocketDisconnect:
        await manager.disconnect(data.sender_id)