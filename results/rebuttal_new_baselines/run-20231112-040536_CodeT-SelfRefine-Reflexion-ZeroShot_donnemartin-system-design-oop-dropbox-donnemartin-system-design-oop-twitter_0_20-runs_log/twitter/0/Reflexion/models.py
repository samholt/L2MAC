from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class User(UserMixin):
	id: int
	username: str
	email: str
	password_hash: str
	bio: str
	location: str
	website: str
	is_private: bool

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

@dataclass
class Post:
	id: int
	user_id: int
	content: str
	image: str

@dataclass
class Follow:
	follower_id: int
	followed_id: int

@dataclass
class Like:
	user_id: int
	post_id: int

@dataclass
class Retweet:
	user_id: int
	post_id: int

@dataclass
class Reply:
	user_id: int
	post_id: int
	content: str

@dataclass
class Message:
	sender_id: int
	receiver_id: int
	content: str

@dataclass
class Notification:
	user_id: int
	content: str
