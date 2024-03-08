from dataclasses import dataclass

@dataclass
class User:
	name: str
	email: str
	password: str

users_db = {}

class UserManagement:
	def register(self, data):
		if data['email'] in users_db:
			return {'status': 'error', 'message': 'Email already exists'}
		user = User(data['name'], data['email'], data['password'])
		users_db[data['email']] = user
		return {'status': 'success', 'message': 'User registered successfully'}

	def login(self, data):
		if data['email'] not in users_db or users_db[data['email']].password != data['password']:
			return {'status': 'error', 'message': 'Invalid email or password'}
		return {'status': 'success', 'message': 'User logged in successfully'}
