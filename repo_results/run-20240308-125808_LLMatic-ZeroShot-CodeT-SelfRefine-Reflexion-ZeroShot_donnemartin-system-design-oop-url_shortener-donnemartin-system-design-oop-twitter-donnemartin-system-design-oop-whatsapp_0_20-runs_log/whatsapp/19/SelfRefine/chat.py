from dataclasses import dataclass, field
from typing import List
import uuid

@dataclass
class Chat:
	name: str
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	users: List[str] = field(default_factory=list)

	def update_chat(self, data):
		self.name = data.get('name', self.name)

	def add_user(self, user):
		self.users.append(user.id)

	def remove_user(self, user):
		self.users.remove(user.id)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'users': self.users
		}
