from dataclasses import dataclass

@dataclass
class User:
	email: str
	username: str
	password: str
	bio: str = ''
	website: str = ''
	location: str = ''
	is_private: bool = False

	def to_dict(self):
		return self.__dict__
