from dataclasses import dataclass
import uuid

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str
	status_message: str
	privacy_settings: dict
	blocked_contacts: list
	groups: list

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = ''
		self.status_message = ''
		self.privacy_settings = {}
		self.blocked_contacts = []
		self.groups = []

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'privacy_settings': self.privacy_settings,
			'blocked_contacts': self.blocked_contacts,
			'groups': self.groups
		}
