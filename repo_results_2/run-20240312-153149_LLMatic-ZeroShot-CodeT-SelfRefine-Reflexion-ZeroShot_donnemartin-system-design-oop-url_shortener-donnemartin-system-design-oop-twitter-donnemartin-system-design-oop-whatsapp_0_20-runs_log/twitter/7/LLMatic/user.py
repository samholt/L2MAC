import hashlib
import jwt
import datetime


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.email = email
		self.username = username
		self.password = self._hash_password(password)
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.following = []
		self.followers = []
		self.blocked_users = []
		self.notifications = []

	def _hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == self._hash_password(password)

	def update_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location

	def follow(self, user):
		if user not in self.following and user not in self.blocked_users:
			self.following.append(user)
			user.followers.append(self)

	def unfollow(self, user):
		if user in self.following:
			self.following.remove(user)
			user.followers.remove(self)

	def block(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)
			if user in self.following:
				self.unfollow(user)

	def unblock(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)

	def receive_notification(self, notification):
		self.notifications.append(notification)

	def generate_jwt(self):
		payload = {
			'username': self.username,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
		}
		token = jwt.encode(payload, 'secret', algorithm='HS256')
		return token

	def validate_jwt(self, token):
		try:
			decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
			return decoded['username'] == self.username
		except jwt.ExpiredSignatureError:
			return False
		except jwt.InvalidTokenError:
			return False
