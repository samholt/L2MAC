from dataclasses import dataclass
import uuid

@dataclass
class Chat:
	id: str
	name: str
	users: list

	def __init__(self, name):
		self.id = str(uuid.uuid4())
		self.name = name
		self.users = []

	def add_user(self, user):
		self.users.append(user)

	def to_dict(self):
		return {'id': self.id, 'name': self.name, 'users': [user.to_dict() for user in self.users]}
