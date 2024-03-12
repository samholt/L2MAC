import uuid
from dataclasses import dataclass
from typing import List

@dataclass
class Message:
	user_id: str
	content: str

@dataclass
class Chat:
	id: str
	name: str
	messages: List[Message]

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.messages = []

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.__dict__ for message in self.messages]}
