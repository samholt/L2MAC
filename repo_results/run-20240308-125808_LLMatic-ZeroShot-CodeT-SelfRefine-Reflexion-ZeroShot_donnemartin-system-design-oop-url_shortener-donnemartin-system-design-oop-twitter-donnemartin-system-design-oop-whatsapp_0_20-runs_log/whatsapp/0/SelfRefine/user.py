from dataclasses import dataclass, field
import uuid

@dataclass
class User:
	email: str
	password: str
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	chats: list = field(default_factory=list)

	def to_dict(self):
		return {'id': self.id, 'email': self.email, 'chats': self.chats}
