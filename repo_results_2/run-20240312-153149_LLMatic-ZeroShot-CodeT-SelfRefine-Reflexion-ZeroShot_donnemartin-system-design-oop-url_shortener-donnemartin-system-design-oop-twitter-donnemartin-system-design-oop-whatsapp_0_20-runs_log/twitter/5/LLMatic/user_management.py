import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# Mock database
users_db = {}

SECRET_KEY = 'YOUR-SECRET-KEY'


def register_user(username, password):
	if username in users_db:
		return {'message': 'User already exists'}
	password_hash = generate_password_hash(password)
	users_db[username] = {'password': password_hash, 'profile': {}, 'visible': True}
	return {'message': 'User registered successfully'}


def authenticate_user(username, password):
	user = users_db.get(username)
	if not user or not check_password_hash(user['password'], password):
		return {'message': 'Invalid username or password'}
	token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY, algorithm='HS256')
	return {'token': token}


def reset_password(username, new_password):
	user = users_db.get(username)
	if not user:
		return {'message': 'User does not exist'}
	new_password_hash = generate_password_hash(new_password)
	users_db[username]['password'] = new_password_hash
	return {'message': 'Password reset successfully'}


def edit_profile(username, profile):
	user = users_db.get(username)
	if not user:
		return {'message': 'User does not exist'}
	users_db[username]['profile'] = profile
	return {'message': 'Profile updated successfully'}


def toggle_visibility(username):
	user = users_db.get(username)
	if not user:
		return {'message': 'User does not exist'}
	users_db[username]['visible'] = not users_db[username]['visible']
	return {'message': 'Profile visibility toggled'}
