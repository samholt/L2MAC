import jwt
import datetime

SECRET_KEY = 'secret'


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website=None, location=None, private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website = website
		self.location = location
		self.private = private
		self.followers = []
		self.following = []
		self.notifications = []

	def check_password(self, password):
		return self.password == password

	def get_reset_token(self, expires_sec=1800):
		payload = {'user_email': self.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_sec)}
		return jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

	@staticmethod
	def verify_reset_token(token):
		try:
			payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
			return users.get(payload['user_email'])
		except:
			return None


class Post:
	def __init__(self, content, images, user, hashtags=[], mentions=[]):
		self.content = content
		self.images = images
		self.user = user
		self.likes = 0
		self.retweets = 0
		self.replies = []
		self.hashtags = hashtags
		self.mentions = mentions


class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content


class Notification:
	def __init__(self, user, message):
		self.user = user
		self.message = message
