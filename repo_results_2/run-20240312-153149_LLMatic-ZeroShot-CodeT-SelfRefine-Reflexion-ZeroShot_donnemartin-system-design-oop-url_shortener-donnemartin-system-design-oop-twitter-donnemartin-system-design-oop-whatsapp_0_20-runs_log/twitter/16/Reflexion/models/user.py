from dataclasses import dataclass, field

@dataclass
class User:
	name: str
	email: str
	password: str
	followers: dict = field(default_factory=dict)
	following: dict = field(default_factory=dict)
	profile_picture: str = ''
	bio: str = ''
	website_link: str = ''
	location: str = ''
	is_private: bool = False
