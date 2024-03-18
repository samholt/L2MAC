from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class Chat:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	users: List[str]
	messages: List[dict] = field(default_factory=list)

	def update_chat(self, data):
		self.users = data.get('users', self.users)
		self.messages = data.get('messages', self.messages)

	def to_dict(self):
		return {
			'id': self.id,
			'users': self.users,
			'messages': self.messages
		}
