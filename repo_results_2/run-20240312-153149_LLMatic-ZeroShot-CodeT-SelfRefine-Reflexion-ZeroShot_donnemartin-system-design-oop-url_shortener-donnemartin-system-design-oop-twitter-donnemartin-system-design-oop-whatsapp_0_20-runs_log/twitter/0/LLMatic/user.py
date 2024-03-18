from werkzeug.security import generate_password_hash, check_password_hash
from collections import Counter


class User:
	users = {}

	def __init__(self, id, email, username, password, profile_picture=None, bio=None, website=None, location=None):
		self.id = id
		self.email = email
		self.username = username
		self.password_hash = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.following = []
		self.followers = []
		self.messages = []
		self.notifications = []
		User.users[self.id] = self

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def get_id(self):
		return str(self.id)

	def edit_profile(self, profile_picture=None, bio=None, website=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website is not None:
			self.website = website
		if location is not None:
			self.location = location

	def follow(self, user_id):
		if user_id not in self.following:
			self.following.append(user_id)
			User.users[user_id].followers.append(self.id)

	def unfollow(self, user_id):
		if user_id in self.following:
			self.following.remove(user_id)
			User.users[user_id].followers.remove(self.id)

	def recommend_users(self):
		recommended_users = [User.users[user_id].following for user_id in self.following]
		recommended_users = [user_id for sublist in recommended_users for user_id in sublist if user_id not in self.following and user_id != self.id]
		recommended_users = Counter(recommended_users).most_common(5)
		return [User.users[user_id[0]] for user_id in recommended_users if user_id[0] in User.users]
