from fastapi import WebSocket
from typing import Dict

class ConnectionManager:
    def __init__(self):
        self.connections: Dict[str, WebSocket] = {}

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        self.connections[username] = websocket

    async def disconnect(self, username: str):
        self.connections.pop(username, None)

    async def send_message(self, recipient: str, message: str):
        websocket = self.connections.get(recipient)
        if websocket:
            await websocket.send_text(message)
