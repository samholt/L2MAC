from dataclasses import dataclass

users = {}

@dataclass
class User:
	username: str
	password: str

	def to_dict(self):
		return {'username': self.username, 'password': self.password}
