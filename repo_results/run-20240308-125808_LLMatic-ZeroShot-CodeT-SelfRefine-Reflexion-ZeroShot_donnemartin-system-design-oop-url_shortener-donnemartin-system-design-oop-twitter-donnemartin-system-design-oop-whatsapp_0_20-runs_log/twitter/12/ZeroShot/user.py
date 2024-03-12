from dataclasses import dataclass

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None

	def to_dict(self):
		return self.__dict__
