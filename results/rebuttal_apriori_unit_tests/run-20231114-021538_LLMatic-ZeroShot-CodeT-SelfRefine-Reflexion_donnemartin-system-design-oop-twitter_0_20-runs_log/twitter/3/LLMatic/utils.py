import jwt
from models import User

users_db = {}


def register_user(username, email, password):
	user_id = len(users_db) + 1
	new_user = User(user_id, username, email, password)
	users_db[user_id] = new_user
	return True


def authenticate_user(email, password):
	for user in users_db.values():
		if user.email == email and user.password == password:
			token = jwt.encode({'user_id': user.id}, 'secret', algorithm='HS256')
			return token
	return False


def edit_profile(user_id, new_bio, new_website, new_location):
	if user_id in users_db:
		user = users_db[user_id]
		user.bio = new_bio
		user.website = new_website
		user.location = new_location
		return True
	return False
