from dataclasses import dataclass

@dataclass
class User:
	id: str
	name: str
	email: str
	password: str
	profile_picture: str
	storage_used: int
	storage_limit: int
