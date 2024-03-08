from dataclasses import dataclass

@dataclass
class User:
	def __init__(self):
		self.email = None
		self.password = None
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = None
		self.blocked_contacts = []
		self.is_online = False

	def register(self, email, password):
		self.email = email
		self.password = password

	def login(self, email, password):
		if self.email == email and self.password == password:
			self.is_online = True
			return True
		return False

	def logout(self):
		self.is_online = False

	def recover_password(self, email):
		if self.email == email:
			return self.password
		return None

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def block_contact(self, contact):
		self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		if contact in self.blocked_contacts:
			self.blocked_contacts.remove(contact)

	def __eq__(self, other):
		if isinstance(other, User):
			return self.email == other.email
		return False
