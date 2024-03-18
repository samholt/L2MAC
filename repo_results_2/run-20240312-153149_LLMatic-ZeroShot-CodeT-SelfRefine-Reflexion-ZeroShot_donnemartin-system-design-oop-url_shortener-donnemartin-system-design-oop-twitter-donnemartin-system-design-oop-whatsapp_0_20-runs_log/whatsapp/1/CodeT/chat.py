from dataclasses import dataclass
import uuid

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

@dataclass
class Chat:
	id: str
	name: str
	users: list
	messages: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.users = []
		self.messages = []

	def add_user(self, user_id):
		self.users.append(user_id)

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'users': self.users, 'messages': [message.to_dict() for message in self.messages]}
