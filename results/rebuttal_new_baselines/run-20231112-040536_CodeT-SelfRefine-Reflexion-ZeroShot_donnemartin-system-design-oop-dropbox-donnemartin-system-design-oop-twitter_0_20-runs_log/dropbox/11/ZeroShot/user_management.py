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
	return {'message': 'User registered successfully'}

def login(data):
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}
	return {'message': 'Invalid credentials'}

def forgot_password(data):
	user = users.get(data['email'])
	if user:
		user.password = data['new_password']
		return {'message': 'Password reset successful'}
	return {'message': 'User not found'}

def profile(data):
	user = users.get(data['email'])
	if user:
		return {'name': user.name, 'email': user.email, 'storage_used': user.storage_used, 'storage_remaining': user.storage_remaining}
	return {'message': 'User not found'}

def change_password(data):
	user = users.get(data['email'])
	if user and user.password == data['old_password']:
		user.password = data['new_password']
		return {'message': 'Password changed successfully'}
	return {'message': 'Invalid credentials'}
