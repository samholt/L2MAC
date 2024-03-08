import hashlib
import time

# Mock database
users_db = {}
posts_db = {}
replies_db = {}


class User:
	def __init__(self, id, username, email, password, profile_picture=None, bio=None, website=None, location=None):
		self.id = id
		self.username = username
		self.email = email
		self.password = self.hash_password(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location

	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == hashlib.sha256(password.encode()).hexdigest()

	def edit_profile(self, profile_picture, bio, website, location):
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		return True


class Post:
	def __init__(self, id, user_id, content):
		self.id = id
		self.user_id = user_id
		self.content = content
		self.timestamp = time.time()
		self.likes = 0
		self.retweets = 0

	def like(self):
		self.likes += 1
		return True

	def retweet(self):
		self.retweets += 1
		return True


class Reply:
	def __init__(self, id, user_id, post_id, content):
		self.id = id
		self.user_id = user_id
		self.post_id = post_id
		self.content = content
		self.timestamp = time.time()


def register_user(username, email, password):
	user_id = len(users_db) + 1
	new_user = User(user_id, username, email, password)
	users_db[user_id] = new_user
	return True


def authenticate_user(email, password):
	for user in users_db.values():
		if user.email == email and user.check_password(password):
			return True
	return False

def edit_user_profile(user_id, profile_picture, bio, website, location):
	if user_id in users_db:
		user = users_db[user_id]
		return user.edit_profile(profile_picture, bio, website, location)
	return False

def create_post(user_id, content):
	if user_id in users_db:
		post_id = len(posts_db) + 1
		new_post = Post(post_id, user_id, content)
		posts_db[post_id] = new_post
		return post_id
	return False

def delete_post(user_id, post_id):
	if post_id in posts_db and posts_db[post_id].user_id == user_id:
		del posts_db[post_id]
		return True
	return False

def like_post(user_id, post_id):
	if post_id in posts_db and user_id in users_db:
		post = posts_db[post_id]
		return post.like()
	return False

def retweet_post(user_id, post_id):
	if post_id in posts_db and user_id in users_db:
		post = posts_db[post_id]
		return post.retweet()
	return False

def create_reply(user_id, post_id, content):
	if post_id in posts_db and user_id in users_db:
		reply_id = len(replies_db) + 1
		new_reply = Reply(reply_id, user_id, post_id, content)
		replies_db[reply_id] = new_reply
		return reply_id
	return False

