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

def profile(data):
	user = users.get(data['email'])
	if user:
		return user.__dict__, 200
	return {'message': 'User not found'}, 404

def change_password(data):
	user = users.get(data['email'])
	if user and user.password == data['old_password']:
		user.password = data['new_password']
		return {'message': 'Password updated successfully'}, 200
	return {'message': 'Invalid email or old password'}, 401
