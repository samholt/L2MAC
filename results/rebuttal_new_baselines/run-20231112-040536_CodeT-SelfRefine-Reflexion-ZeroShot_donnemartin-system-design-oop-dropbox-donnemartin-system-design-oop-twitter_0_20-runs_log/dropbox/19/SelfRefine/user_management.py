from dataclasses import dataclass
import jwt
import datetime

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str
	storage_used: int
	storage_remaining: int

users = {}
SECRET_KEY = 'secret'


def register(data):
	if data['email'] in users:
		return {'message': 'User with this email already exists'}, 400
	user = User(**data)
	users[user.email] = user
	return {'message': 'User registered successfully'}, 201

def login(data):
	user = users.get(data['email'])
	if user and user.password == data['password']:
		token = jwt.encode({'user': user.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
		return {'token': token.decode('UTF-8')}, 200
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
		user.profile_picture = data.get('profile_picture', user.profile_picture)
		return {'message': 'Profile updated successfully'}, 200
	return {'message': 'User not found'}, 404
