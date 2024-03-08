from dataclasses import dataclass
from models.user import User

@dataclass
class DirectMessage:
	sender: User
	receiver: User
	message: str
