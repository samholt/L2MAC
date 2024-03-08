from dataclasses import dataclass
from uuid import uuid4

@dataclass
class Message:
	id: str = field(default_factory=lambda: str(uuid4()))
	user_id: str
	chat_id: str
	content: str

	def to_dict(self):
		return {'id': self.id, 'user_id': self.user_id, 'chat_id': self.chat_id, 'content': self.content}
