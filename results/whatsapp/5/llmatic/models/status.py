from dataclasses import dataclass
from models.user import User

@dataclass
class Status:
	id: str
	user: User
	content: str
	visibility_settings: dict
