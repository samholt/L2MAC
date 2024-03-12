from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User:
	email: str
	username: str
	_password: str

	def __post_init__(self):
		self._password = generate_password_hash(self._password)

	def check_password(self, password):
		return check_password_hash(self._password, password)

	def to_dict(self):
		return {'email': self.email, 'username': self.username}
