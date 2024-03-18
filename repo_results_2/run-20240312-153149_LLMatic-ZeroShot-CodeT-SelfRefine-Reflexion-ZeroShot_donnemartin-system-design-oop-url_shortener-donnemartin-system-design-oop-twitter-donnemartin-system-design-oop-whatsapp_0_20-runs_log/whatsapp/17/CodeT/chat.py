from dataclasses import dataclass
from typing import Dict, List
from user import User
import uuid

@dataclass
class Message:
	id: str
	user: User
	content: str

	def __init__(self, user: User, content: str):
		self.id = str(uuid.uuid4())
		self.user = user
		self.content = content

	def to_dict(self) -> Dict:
		return {'id': self.id, 'user': self.user.to_dict(), 'content': self.content}

@dataclass
class Chat:
	id: str
	name: str
	users: List[User]
	messages: List[Message]

	def __init__(self, name: str):
		self.id = str(uuid.uuid4())
		self.name = name
		self.users = []
		self.messages = []

	def add_user(self, user: User):
		self.users.append(user)

	def send_message(self, user: User, content: str) -> Message:
		message = Message(user, content)
		self.messages.append(message)
		return message

	def to_dict(self) -> Dict:
		return {'id': self.id, 'name': self.name, 'users': [user.to_dict() for user in self.users], 'messages': [message.to_dict() for message in self.messages]}
