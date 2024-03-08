from dataclasses import dataclass

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = ''
	storage_used: int = 0
	storage_remaining: int = 100
