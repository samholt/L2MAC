from dataclasses import dataclass
import uuid

@dataclass

class User:
	id: str
	email: str
	password: str

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password

	def to_dict(self):
		return {'id': self.id, 'email': self.email}
