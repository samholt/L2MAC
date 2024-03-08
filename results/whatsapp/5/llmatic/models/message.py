from dataclasses import dataclass
from typing import Union
from .user import User

@dataclass
class Message:
	id: str
	sender: User
	receiver: Union[User, str]
	content: Union[str, bytes]
	read_receipt: bool

