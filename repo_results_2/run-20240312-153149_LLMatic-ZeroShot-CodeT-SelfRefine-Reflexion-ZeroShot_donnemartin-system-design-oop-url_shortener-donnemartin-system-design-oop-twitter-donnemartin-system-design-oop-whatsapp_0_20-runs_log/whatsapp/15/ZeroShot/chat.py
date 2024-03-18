from dataclasses import dataclass, field
import uuid

@dataclass
class Chat:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	name: str
	users: list = field(default_factory=list)

	def add_user(self, user):
		self.users.append(user.id)

	def remove_user(self, user):
		self.users.remove(user.id)

	def update_chat(self, data):
		self.name = data.get('name', self.name)

	def to_dict(self):
		return {
			'id': self.id,
			'name': self.name,
			'users': self.users
		}
