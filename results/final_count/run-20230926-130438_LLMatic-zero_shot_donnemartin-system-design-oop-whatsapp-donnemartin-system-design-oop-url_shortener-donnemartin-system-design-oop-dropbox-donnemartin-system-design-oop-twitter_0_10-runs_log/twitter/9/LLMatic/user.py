import jwt
import datetime

# Mock database
users_db = {}


class User:
	def __init__(self, email, username, password, profile_picture=None, bio=None, website_link=None, location=None, private=False):
		self.email = email
		self.username = username
		self.password = password
		self.profile_picture = profile_picture
		self.bio = bio
		self.website_link = website_link
		self.location = location
		self.private = private

	def register(self):
		if self.email in users_db:
			return 'User already exists'
		else:
			users_db[self.email] = self
			return 'User registered successfully'

	def authenticate(self, password):
		if self.password == password:
			token = jwt.encode({'user': self.email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 'secret')
			return token
		else:
			return 'Invalid password'

	def reset_password(self, new_password):
		self.password = new_password
		return 'Password reset successfully'

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		self.profile_picture = profile_picture if profile_picture else self.profile_picture
		self.bio = bio if bio else self.bio
		self.website_link = website_link if website_link else self.website_link
		self.location = location if location else self.location
		return 'Profile updated successfully'

	def toggle_privacy(self):
		self.private = not self.private
		return 'Privacy setting updated successfully'
