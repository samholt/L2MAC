import jwt
import hashlib


class User:
	def __init__(self, username, email, password, profile_picture=None, bio=None, website_link=None, location=None):
		self.username = username
		self.email = email
		self.password = self._encrypt_password(password)
		self.jwt_token = self._generate_jwt_token()
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.followers = []
		self.following = []
		self.notifications = []

	def _encrypt_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def _generate_jwt_token(self):
		return jwt.encode({'username': self.username, 'email': self.email}, 'secret', algorithm='HS256')

	def edit_profile(self, new_bio, new_website, new_location):
		self.bio = new_bio
		self.website_link = new_website
		self.location = new_location
		return True

	def follow_user(self, target_user):
		if target_user not in self.following:
			self.following.append(target_user)
			target_user.followers.append(self)
			self.notifications.append(f'You started following {target_user.username}')
			return True
		return False

	def unfollow_user(self, target_user):
		if target_user in self.following:
			self.following.remove(target_user)
			target_user.followers.remove(self)
			self.notifications.append(f'You stopped following {target_user.username}')
			return True
		return False

	def get_notifications(self):
		notifications = self.notifications
		self.notifications = []
		return notifications


users = {}


def register_user(username, email, password):
	if username in users or email in users:
		return False
	users[username] = User(username, email, password)
	return True


def authenticate_user(email, password):
	for user in users.values():
		if user.email == email and user.password == hashlib.sha256(password.encode()).hexdigest():
			return user.jwt_token
	return False

def edit_user_profile(username, new_bio, new_website, new_location):
	if username in users:
		return users[username].edit_profile(new_bio, new_website, new_location)
	return False

def search_users(keyword):
	return [user for user in users.values() if keyword in user.username or keyword in user.email]

def follow_user(username, target_username):
	if username in users and target_username in users:
		return users[username].follow_user(users[target_username])
	return False

def unfollow_user(username, target_username):
	if username in users and target_username in users:
		return users[username].unfollow_user(users[target_username])
	return False

def get_user_notifications(username):
	if username in users:
		return users[username].get_notifications()
	return False

