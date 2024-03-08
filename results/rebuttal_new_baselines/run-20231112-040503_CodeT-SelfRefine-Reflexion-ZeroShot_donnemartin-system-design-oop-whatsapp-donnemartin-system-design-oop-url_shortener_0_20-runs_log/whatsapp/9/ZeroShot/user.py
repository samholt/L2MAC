from dataclasses import dataclass, field
from typing import List
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User:
	id: str
	email: str
	password_hash: str
	profile_picture: str = field(default=None)
	status_message: str = field(default=None)
	blocked_contacts: List[str] = field(default_factory=list)

	def __init__(self, email, password):
		self.id = generate_id()
		self.email = email
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.status_message = data.get('status_message', self.status_message)

	def block_contact(self, contact):
		self.blocked_contacts.append(contact.id)

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'blocked_contacts': self.blocked_contacts
		}

	def generate_id():
		return str(uuid.uuid4())
