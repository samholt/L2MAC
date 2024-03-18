from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class User:
	email: str
	username: str
	_password: str
	bio: str = ''
	website: str = ''
	location: str = ''
	private: bool = False

	def __post_init__(self):
		self._password = generate_password_hash(self._password)

	def check_password(self, password):
		return check_password_hash(self._password, password)

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)

	def to_dict(self):
		return {key: value for key, value in self.__dict__.items() if key != '_password'}
