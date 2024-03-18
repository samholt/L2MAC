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
	contacts: dict

	def __init__(self, email, password):
		self.id = str(uuid.uuid4())
		self.email = email
		self.password = password
		self.profile_picture = ''
		self.status_message = ''
		self.privacy_settings = {}
		self.contacts = {}

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile_picture': self.profile_picture,
			'status_message': self.status_message,
			'privacy_settings': self.privacy_settings,
			'contacts': {id: contact.to_dict() for id, contact in self.contacts.items()}
		}
