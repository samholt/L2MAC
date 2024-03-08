from dataclasses import dataclass, field
from typing import List
from user import User

@dataclass
class Message:
	id: str
	user: User
	content: str

	def __init__(self, user, content):
		self.id = generate_id()
		self.user = user
		self.content = content

	def to_dict(self):
		return {
			'id': self.id,
			'user': self.user.to_dict(),
			'content': self.content
		}

	def generate_id():
		return str(uuid.uuid4())

@dataclass
class Chat:
	id: str
	name: str
	messages: List[Message] = field(default_factory=list)

	def __init__(self, name):
		self.id = generate_id()
		self.name = name

	def send_message(self, user, content):
		message = Message(user, content)
		self.messages.append(message)
		return message

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'messages': [message.to_dict() for message in self.messages]
		}

	def generate_id():
		return str(uuid.uuid4())
