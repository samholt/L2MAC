from dataclasses import dataclass, field

@dataclass
class User:
	email: str
	username: str
	password: str
	profile_picture: str = field(default=None)
	bio: str = field(default=None)
	website_link: str = field(default=None)
	location: str = field(default=None)
	private: bool = field(default=False)

	def to_dict(self):
		return self.__dict__

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if hasattr(self, key):
				setattr(self, key, value)
