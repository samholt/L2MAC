from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class User:
	id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)
	email: str
	password: str
	chats: List[str] = field(default_factory=list)

	def to_dict(self):
		return {'id': self.id, 'email': self.email, 'chats': self.chats}
