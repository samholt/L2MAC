from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

@dataclass
class User:
	id: str
	email: str
	_password: str

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self._password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self._password, password)

	def to_dict(self):
		return {'id': self.id, 'email': self.email}
