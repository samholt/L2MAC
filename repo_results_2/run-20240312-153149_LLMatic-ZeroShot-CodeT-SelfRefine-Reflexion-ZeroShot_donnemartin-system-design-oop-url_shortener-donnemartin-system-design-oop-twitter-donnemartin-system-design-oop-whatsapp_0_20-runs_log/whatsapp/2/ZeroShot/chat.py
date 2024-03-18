import uuid
from dataclasses import dataclass
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
		return {
			'id': self.id,
			'user_id': self.user.id,
			'content': self.content
		}

@dataclass
class Chat:
	id: str
	name: str
	users: list
	messages: list

	def __init__(self, name, user_ids):
		self.id = str(uuid.uuid4())
		self.name = name
		self.users = user_ids
		self.messages = []

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'users': self.users,
			'messages': [message.to_dict() for message in self.messages]
		}

	def update_chat(self, data):
		self.name = data.get('name', self.name)
		self.users = data.get('users', self.users)

	def send_message(self, user_id, content):
		message = Message(user_id, content)
		self.messages.append(message)
		return message.to_dict()
