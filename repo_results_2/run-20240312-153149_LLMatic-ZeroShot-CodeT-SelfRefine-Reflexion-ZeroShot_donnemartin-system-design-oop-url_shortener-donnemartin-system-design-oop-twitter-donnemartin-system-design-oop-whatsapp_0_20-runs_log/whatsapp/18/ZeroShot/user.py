from dataclasses import dataclass, field
from typing import List
import uuid
import hashlib

@dataclass
class User:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	email: str
	password: str
	profile_picture: str = ''
	status_message: str = ''
	blocked_users: List[str] = field(default_factory=list)

	def check_password(self, password):
		return self.password == hashlib.sha256(password.encode()).hexdigest()

	def reset_password(self):
		self.password = hashlib.sha256('default'.encode()).hexdigest()

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.status_message = data.get('status_message', self.status_message)

	def block_user(self, user):
		self.blocked_users.append(user.id)

	def unblock_user(self, user):
		self.blocked_users.remove(user.id)

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'blocked_users': self.blocked_users
		}
