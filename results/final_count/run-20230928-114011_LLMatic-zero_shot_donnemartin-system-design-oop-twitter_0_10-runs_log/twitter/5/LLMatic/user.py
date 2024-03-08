import jwt
from dataclasses import dataclass
from datetime import datetime, timedelta

SECRET_KEY = 'secret'

@dataclass
class User:
	email: str
	username: str
	password: str

	def generate_auth_token(self):
		payload = {
			'exp': datetime.utcnow() + timedelta(minutes=60),
			'iat': datetime.utcnow(),
			'sub': self.username
		}
		return jwt.encode(
			payload,
			SECRET_KEY,
			algorithm='HS256'
		)

	def reset_password(self, new_password):
		self.password = new_password
		return self

@dataclass
class UserProfile:
	user: User
	profile_picture: str
	bio: str
	website_link: str
	location: str
	is_private: bool = False

	def edit_profile(self, profile_picture=None, bio=None, website_link=None, location=None):
		if profile_picture is not None:
			self.profile_picture = profile_picture
		if bio is not None:
			self.bio = bio
		if website_link is not None:
			self.website_link = website_link
		if location is not None:
			self.location = location
		return self

	def toggle_privacy(self):
		self.is_private = not self.is_private
		return self
