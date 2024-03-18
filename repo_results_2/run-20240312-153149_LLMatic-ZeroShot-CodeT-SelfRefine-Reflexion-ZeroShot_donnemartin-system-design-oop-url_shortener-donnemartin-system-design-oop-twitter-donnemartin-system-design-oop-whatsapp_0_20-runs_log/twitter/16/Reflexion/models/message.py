from dataclasses import dataclass, field
from .user import User

@dataclass
class Message:
	sender: User
	receiver: User
	content: str
