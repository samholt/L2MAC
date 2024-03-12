import uuid
from dataclasses import dataclass
from message import Message

@dataclass
class Chat:
	id: str
	name: str
	messages: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.messages = []

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.to_dict() for message in self.messages]}
