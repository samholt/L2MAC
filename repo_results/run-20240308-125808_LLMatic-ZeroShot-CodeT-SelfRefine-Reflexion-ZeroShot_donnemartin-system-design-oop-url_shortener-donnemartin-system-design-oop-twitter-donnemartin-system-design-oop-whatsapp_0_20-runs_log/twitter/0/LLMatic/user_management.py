from social_interaction import Notification

class User:
	def __init__(self, email, username, password):
		self.email = email
		self.username = username
		self.password = password
		self.following = []
		self.blocked_users = []
		self.notifications = []

	def follow(self, user):
		self.following.append(user)

	def unfollow(self, user):
		self.following.remove(user)

	def block(self, user):
		self.blocked_users.append(user)

	def unblock(self, user):
		self.blocked_users.remove(user)

	def create_notification(self, notification_type, post):
		self.notifications.append(Notification(self, notification_type, post))

	def like(self, post):
		post.like(self)

	def retweet(self, post):
		post.retweet(self)

	def reply(self, post, content):
		post.reply(self, content)

	def recommend_users(self, users):
		# Mock implementation as interests, activity, and mutual followers data is not available
		return users


class UserManagement:
	def __init__(self):
		self.users = []

	def register(self, email, username, password):
		self.users.append(User(email, username, password))

	def login(self, email, password):
		for user in self.users:
			if user.email == email and user.password == password:
				return user
		return None

	def search_users_by_username(self, username):
		for user in self.users:
			if user.username == username:
				return user
		return None
