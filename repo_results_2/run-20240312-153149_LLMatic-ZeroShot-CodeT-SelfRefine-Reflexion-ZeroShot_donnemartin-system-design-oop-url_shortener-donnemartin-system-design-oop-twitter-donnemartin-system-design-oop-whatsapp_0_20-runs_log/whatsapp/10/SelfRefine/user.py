from dataclasses import dataclass
import uuid

@dataclass
class User:
	id: str
	email: str
	password: str

	def __init__(self, email, password, id=None):
		self.id = str(uuid.uuid4()) if id is None else id
		self.email = email
		self.password = password

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email
		}
