from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from user import User

class MessageType(Enum):
    TEXT = 'text'
    IMAGE = 'image'
    DOCUMENT = 'document'

class MessageStatus(Enum):
    DELIVERED = 'delivered'
    READ = 'read'

@dataclass
class Message:
    message_id: int
    sender: User
    receiver: User
    content: str
    timestamp: datetime
    status: MessageStatus
    type: MessageType
