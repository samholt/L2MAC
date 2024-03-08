from dataclasses import dataclass
from .user import User
from .message import Message
from typing import List

@dataclass
class Chat:
    chat_id: int
    participants: List[User]
    messages: List[Message]