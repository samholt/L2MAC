from dataclasses import dataclass

@dataclass
class User:
	name: str
	email: str
	password: str
	storage_used: int
	storage_remaining: int

users = {}


def register(data):
	user = User(**data)
	users[user.email] = user
	return user

def login(data):
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return user
	return None

def get_profile(data):
	return users.get(data['email'])
