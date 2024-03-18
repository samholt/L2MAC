from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass
import uuid

@dataclass
class User:
	username: str
	email: str
	password: str
	profile_picture: str = None
	bio: str = None
	website_link: str = None
	location: str = None
	is_private: bool = False

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.bio = data.get('bio', self.bio)
		self.website_link = data.get('website_link', self.website_link)
		self.location = data.get('location', self.location)
		self.is_private = data.get('is_private', self.is_private)

	def to_dict(self):
		return {
			'username': self.username,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'bio': self.bio,
			'website_link': self.website_link,
			'location': self.location,
			'is_private': self.is_private
		}

@dataclass
class Post:
	username: str
	content: str
	image_url: str = None
	id: str = uuid.uuid4().hex

@dataclass
class Comment:
	username: str
	post_id: str
	content: str
	id: str = uuid.uuid4().hex

@dataclass
class Message:
	sender_username: str
	recipient_username: str
	content: str
	id: str = uuid.uuid4().hex

@dataclass
class Notification:
	recipient_username: str
	content: str
	id: str = uuid.uuid4().hex
