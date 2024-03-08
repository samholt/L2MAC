from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Mock database
users_db = {}
posts_db = {}
notifications_db = {}


class User:
	def __init__(self, id, username, email, password, profile_picture=None, bio=None, website_link=None, location=None, interests=None, activity_level=0):
		self.id = id
		self.username = username
		self.email = email
		self.password_hash = generate_password_hash(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.interests = interests if interests else []
		self.activity_level = activity_level
		self.following = []
		self.followers = []
		self.blocked = []
		self.notifications = []

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def follow(self, user):
		if user not in self.following and user not in self.blocked:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def block(self, user):
		if user in self.following:
			self.unfollow(user)
		self.blocked.append(user)

	def unblock(self, user):
		if user in self.blocked:
			self.blocked.remove(user)

	def add_notification(self, notification):
		self.notifications.append(notification)

	def like_post(self, post):
		self.create_notification(post.user_id, f'{self.username} liked your post.')
		post.likes += 1

	def retweet_post(self, post):
		self.create_notification(post.user_id, f'{self.username} retweeted your post.')
		post.retweets += 1

	def reply_to_post(self, post, reply):
		self.create_notification(post.user_id, f'{self.username} replied to your post.')

	def mention_user(self, user):
		self.create_notification(user.id, f'{self.username} mentioned you in a post.')

	def create_notification(self, user_id, message):
		notification = Notification(len(notifications_db) + 1, user_id, message)
		notifications_db[notification.id] = notification
		self.add_notification(notification)
		users_db[user_id].notifications.append(notification)


class Post:
	def __init__(self, id, user_id, text, image=None, timestamp=None):
		self.id = id
		self.user_id = user_id
		self.text = text
		self.image = image
		self.timestamp = timestamp if timestamp else datetime.utcnow()
		self.likes = 0
		self.retweets = 0
		self.reply_to = None
		self.hashtags = [word for word in text.split() if word.startswith('#')]

	def mention_user(self, user):
		users_db[self.user_id].create_notification(user.id, f'{users_db[self.user_id].username} mentioned you in a post.')


class Message:
	def __init__(self, id, sender_id, receiver_id, text, timestamp=None):
		self.id = id
		self.sender_id = sender_id
		self.receiver_id = receiver_id
		self.text = text
		self.timestamp = timestamp if timestamp else datetime.utcnow()


class Notification:
	def __init__(self, id, user_id, message, timestamp=None):
		self.id = id
		self.user_id = user_id
		self.message = message
		self.timestamp = timestamp if timestamp else datetime.utcnow()

