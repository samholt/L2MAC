from dataclasses import dataclass

@dataclass
class User:
	id: int
	username: str
	email: str
	password: str
	bio: str = ''
	website: str = ''
	location: str = ''
	is_private: bool = False
	followers: list = None
	following: list = None
	
	def __post_init__(self):
		self.followers = self.followers or []
		self.following = self.following or []
