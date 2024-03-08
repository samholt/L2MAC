from uuid import uuid4

class User:
	def __init__(self, email, password):
		self.id = str(uuid4())
		self.email = email
		self.password = password
		self.profile = {}
		self.contacts = []

	def to_dict(self):
		return {
			'id': self.id,
			'email': self.email,
			'profile': self.profile,
			'contacts': [contact.id for contact in self.contacts]
		}

	def update_profile(self, data):
		self.profile.update(data)

	def add_contact(self, contact):
		self.contacts.append(contact)
