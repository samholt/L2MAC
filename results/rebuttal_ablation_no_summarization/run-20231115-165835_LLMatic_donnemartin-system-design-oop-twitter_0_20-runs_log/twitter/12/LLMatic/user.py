import jwt
import datetime
import random

# Mock database
users_db = {}
posts_db = {}

SECRET_KEY = 'secret'


class User:
	def __init__(self, username, email, password, profile_picture=None, bio=None, website_link=None, location=None, is_private=False):
		self.username = username
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.is_private = is_private
		self.following = []
		self.blocked_users = set()

	@staticmethod
	def register(username, email, password):
		if username in users_db:
			return False
		users_db[username] = User(username, email, password)
		return True

	@staticmethod
	def authenticate(username, password):
		user = users_db.get(username)
		if user and user.password == password:
			token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
			return token
		return None

	@staticmethod
	def update_profile(username, profile_picture, bio, website_link, location, is_private):
		user = users_db.get(username)
		if user:
			user.profile_picture = profile_picture
			user.bio = bio
			user.website_link = website_link
			user.location = location
			user.is_private = is_private
			return True
		return False

	@staticmethod
	def follow(username, user_to_follow):
		user = users_db.get(username)
		if user and user_to_follow in users_db and user_to_follow not in user.following:
			user.following.append(user_to_follow)
			return True
		return False

	@staticmethod
	def unfollow(username, user_to_unfollow):
		user = users_db.get(username)
		if user and user_to_unfollow in user.following:
			user.following.remove(user_to_unfollow)
			return True
		return False

	@staticmethod
	def get_timeline(username):
		user = users_db.get(username)
		if user:
			timeline_posts = [post for post in posts_db.values() if post.username in user.following]
			return timeline_posts
		return None

	@staticmethod
	def recommend_users_to_follow(username):
		user = users_db.get(username)
		if user:
			all_users = list(users_db.keys())
			all_users.remove(username)
			for followed_user in user.following:
				if followed_user in all_users:
					all_users.remove(followed_user)
			return random.sample(all_users, min(5, len(all_users)))
		return None
