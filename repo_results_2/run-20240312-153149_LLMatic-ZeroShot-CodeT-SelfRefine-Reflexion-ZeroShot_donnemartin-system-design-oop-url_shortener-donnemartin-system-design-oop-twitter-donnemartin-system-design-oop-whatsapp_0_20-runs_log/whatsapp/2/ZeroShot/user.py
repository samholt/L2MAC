import uuid
from dataclasses import dataclass

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	blocked_users: list

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = ''
		self.status_message = ''
		self.blocked_users = []

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'blocked_users': [user.id for user in self.blocked_users]
		}

	def reset_password(self):
		self.password = str(uuid.uuid4())[:8]

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.status_message = data.get('status_message', self.status_message)

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
