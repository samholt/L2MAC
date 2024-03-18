from dataclasses import dataclass, field
import uuid

@dataclass
class User:
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	blocked_users: list = field(default_factory=list)
	id: str = field(default_factory=lambda: str(uuid.uuid4()))

	def __init__(self, email, password):
		self.email = email
		self.password = password

	def reset_password(self):
		self.password = 'password'

	def update_profile(self, profile_picture, status_message):
		self.profile_picture = profile_picture
		self.status_message = status_message

	def block_user(self, user_id):
		self.blocked_users.append(user_id)

	def unblock_user(self, user_id):
		self.blocked_users.remove(user_id)

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'blocked_users': self.blocked_users
		}
