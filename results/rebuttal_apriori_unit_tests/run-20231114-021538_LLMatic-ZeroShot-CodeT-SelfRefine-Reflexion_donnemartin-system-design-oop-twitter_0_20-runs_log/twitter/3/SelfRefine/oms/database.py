from user import User
from post import Post
from message import Message
from notification import Notification
from trending import Trending


class Database:
	def __init__(self):
		self.users = {}
		self.posts = {}
		self.messages = {}
		self.notifications = {}
		self.trending = {}
	
	def add_user(self, user: User):
		self.users[user.id] = user
	
	def add_post(self, post: Post):
		self.posts[post.id] = post
	
	def add_message(self, message: Message):
		self.messages[message.id] = message
	
	def add_notification(self, notification: Notification):
		self.notifications[notification.id] = notification
	
	def add_trending(self, trending: Trending):
		self.trending[trending.id] = trending
