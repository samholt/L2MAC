from dataclasses import dataclass
from .user import User

@dataclass
class Message:
    message_id: int
    sender: User
    receiver: User
    content: str
    timestamp: str
    status: str