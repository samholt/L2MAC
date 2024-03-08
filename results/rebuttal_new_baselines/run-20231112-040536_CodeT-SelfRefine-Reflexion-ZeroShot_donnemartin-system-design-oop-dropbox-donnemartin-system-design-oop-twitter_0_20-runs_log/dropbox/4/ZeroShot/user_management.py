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
	return {'message': 'User registered successfully'}, 201

def login(data):
	user = users.get(data['email'])
	if user and user.password == data['password']:
		return {'message': 'Login successful'}, 200
	return {'message': 'Invalid email or password'}, 401

def forgot_password(data):
	user = users.get(data['email'])
	if user:
		user.password = data['new_password']
		return {'message': 'Password updated successfully'}, 200
	return {'message': 'User not found'}, 404

def get_profile():
	return [user.__dict__ for user in users.values()], 200

def update_profile(data):
	user = users.get(data['email'])
	if user:
		user.name = data.get('name', user.name)
		user.password = data.get('password', user.password)
		return {'message': 'Profile updated successfully'}, 200
	return {'message': 'User not found'}, 404
