from dataclasses import dataclass, field
import uuid

@dataclass
class User:
	id: str = field(default_factory=lambda: str(uuid.uuid4()))
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	blocked_contacts: list = field(default_factory=list)

	def reset_password(self):
		self.password = 'new_password'

	def update_profile(self, data):
		self.profile_picture = data.get('profile_picture', self.profile_picture)
		self.status_message = data.get('status_message', self.status_message)

	def block_contact(self, contact):
		self.blocked_contacts.append(contact.id)

	def unblock_contact(self, contact):
		self.blocked_contacts.remove(contact.id)

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'blocked_contacts': self.blocked_contacts
		}
