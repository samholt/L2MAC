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
	return {'status': 'success', 'message': 'User registered successfully'}

def login(data):
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'status': 'success', 'message': 'User logged in successfully'}
	return {'status': 'error', 'message': 'Invalid email or password'}

def forgot_password(data):
	user = users.get(data['email'])
	if user:
		user.password = data['new_password']
		return {'status': 'success', 'message': 'Password changed successfully'}
	return {'status': 'error', 'message': 'User not found'}

def profile(data):
	user = users.get(data['email'])
	if user:
		return {'status': 'success', 'data': user.__dict__}
	return {'status': 'error', 'message': 'User not found'}

def change_password(data):
	user = users.get(data['email'])
	if user and user.password == data['old_password']:
		user.password = data['new_password']
		return {'status': 'success', 'message': 'Password changed successfully'}
	return {'status': 'error', 'message': 'Invalid email or password'}
