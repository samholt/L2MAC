import uuid
from dataclasses import dataclass
from message import Message

@dataclass
class Chat:
	id: str
	name: str
	messages: list
	users: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.messages = []
		self.users = []

	def add_user(self, user):
		self.users.append(user)

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'messages': [message.to_dict() for message in self.messages], 'users': [user.to_dict() for user in self.users]}
