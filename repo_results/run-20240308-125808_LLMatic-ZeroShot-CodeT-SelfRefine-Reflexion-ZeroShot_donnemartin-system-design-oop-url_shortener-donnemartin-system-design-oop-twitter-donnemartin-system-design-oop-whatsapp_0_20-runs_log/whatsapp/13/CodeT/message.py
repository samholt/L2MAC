import uuid
from dataclasses import dataclass

@dataclass
class Message:
	id: str
	user_id: str
	content: str

	def __init__(self, user_id, content):
		self.id = str(uuid.uuid4())
		self.user_id = user_id
		self.content = content

	def to_dict(self):
		return {'id': self.id, 'user_id': self.user_id, 'content': self.content}
