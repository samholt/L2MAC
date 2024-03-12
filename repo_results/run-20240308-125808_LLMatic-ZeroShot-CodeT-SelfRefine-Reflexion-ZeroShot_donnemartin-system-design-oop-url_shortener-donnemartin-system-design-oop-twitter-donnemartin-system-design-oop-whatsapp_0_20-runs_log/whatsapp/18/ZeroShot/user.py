from dataclasses import dataclass, field
from typing import List
from uuid import uuid4
from message import Message

@dataclass
class User:
	id: str = field(default_factory=lambda: str(uuid4()))
	email: str
	password: str
	chats: List[str] = field(default_factory=list)

	def to_dict(self):
		return {'id': self.id, 'email': self.email, 'chats': self.chats}

	def send_message(self, chat, content):
		message = Message(self.id, content)
		chat.messages.append(message)
		return message
