from dataclasses import dataclass

users_db = {}

@dataclass
class User:
	email: str
	password: str
