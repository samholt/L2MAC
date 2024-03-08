from dataclasses import dataclass

@dataclass
class User:
	name: str
	email: str
	password: str

	def to_dict(self):
		return {'name': self.name, 'email': self.email}
