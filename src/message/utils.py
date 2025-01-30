from fastapi import WebSocket

from .service import MessageService

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}
        
    async def connect(self, websocket: WebSocket, sender_id: int):
        await websocket.accept()
        self.active_connections[sender_id] = websocket
        
    async def disconnect(self, user_id: int):
        del self.active_connections[user_id]
        
    async def send_message(self, text: str, receiver_id: int):
        if receiver_id in self.active_connections:
            await self.active_connections[receiver_id].send_text(text)
            return True
        else:
            return False
        
    async def receive_message(self, sender_id: int):
        return await self.active_connections[sender_id].receive_text()