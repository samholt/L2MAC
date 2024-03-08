from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class Message:
	user_id: str
	content: str
	id: str = field(default_factory=lambda: str(uuid.uuid4()))

	def to_dict(self):
		return {'id': self.id, 'user_id': self.user_id, 'content': self.content}

@dataclass
class Chat:
	name: str
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	messages: List[Message] = field(default_factory=list)

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.to_dict() for message in self.messages]}
