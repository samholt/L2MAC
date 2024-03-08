from dataclasses import dataclass

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str
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
	else:
		return {'status': 'error', 'message': 'Invalid email or password'}

def forgot_password(data):
	user = users.get(data['email'])
	if user:
		user.password = data['new_password']
		return {'status': 'success', 'message': 'Password changed successfully'}
	else:
		return {'status': 'error', 'message': 'User not found'}

def get_profile(data):
	user = users.get(data['email'])
	if user:
		return user.__dict__
	else:
		return {'status': 'error', 'message': 'User not found'}

def update_profile(data):
	user = users.get(data['email'])
	if user:
		user.name = data.get('name', user.name)
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		return {'status': 'success', 'message': 'Profile updated successfully'}
	else:
		return {'status': 'error', 'message': 'User not found'}
