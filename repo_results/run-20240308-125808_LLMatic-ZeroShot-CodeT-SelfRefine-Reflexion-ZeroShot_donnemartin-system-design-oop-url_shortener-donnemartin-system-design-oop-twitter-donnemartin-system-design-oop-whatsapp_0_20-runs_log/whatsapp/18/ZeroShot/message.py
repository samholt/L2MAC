from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Message:
	id: str = field(default_factory=lambda: str(uuid4()))
	sender_id: str
	content: str

	def to_dict(self):
		return {'id': self.id, 'sender_id': self.sender_id, 'content': self.content}
