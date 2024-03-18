from dataclasses import dataclass, field
from .user import User

@dataclass
class Notification:
	user: User
	content: str
