from dataclasses import dataclass
import uuid
from user import User

@dataclass
class Message:
	id: str
	user: User
	content: str

	def __init__(self, user, content):
		self.id = str(uuid.uuid4())
		self.user = user
		self.content = content

	def to_dict(self):
		return {'id': self.id, 'user': self.user.to_dict(), 'content': self.content}

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

	def add_user(self, user):
		self.users.append(user)

	def send_message(self, user, content):
		message = Message(user, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'users': [user.to_dict() for user in self.users], 'messages': [message.to_dict() for message in self.messages]}
