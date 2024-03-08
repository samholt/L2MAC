import jwt
from models import User
from werkzeug.security import check_password_hash

# Mock database
users_db = {}


def register(username, email, password):
	user = User(len(users_db) + 1, username, email, password)
	users_db[username] = user
	return user


def authenticate(username, password):
	user = users_db.get(username)
	if user and user.check_password(password):
		token = jwt.encode({'username': username}, 'secret', algorithm='HS256')
		return token
	else:
		return 'Invalid username or password.'

def edit_profile(username, profile_picture=None, bio=None, website_link=None, location=None):
	user = users_db.get(username)
	if user:
		user.profile_picture = profile_picture
		user.bio = bio
		user.website_link = website_link
		user.location = location
		return user
	else:
		return 'User not found.'

def follow_user(username, user_to_follow):
	user = users_db.get(username)
	if user and user_to_follow in users_db:
		user.follow(users_db[user_to_follow])
		return user
	else:
		return 'User not found.'

def unfollow_user(username, user_to_unfollow):
	user = users_db.get(username)
	if user and user_to_unfollow in users_db:
		user.unfollow(users_db[user_to_unfollow])
		return user
	else:
		return 'User not found.'

def block_user(username, user_to_block):
	user = users_db.get(username)
	if user and user_to_block in users_db:
		user.block(users_db[user_to_block])
		return user
	else:
		return 'User not found.'

def unblock_user(username, user_to_unblock):
	user = users_db.get(username)
	if user and user_to_unblock in users_db:
		user.unblock(users_db[user_to_unblock])
		return user
	else:
		return 'User not found.'

