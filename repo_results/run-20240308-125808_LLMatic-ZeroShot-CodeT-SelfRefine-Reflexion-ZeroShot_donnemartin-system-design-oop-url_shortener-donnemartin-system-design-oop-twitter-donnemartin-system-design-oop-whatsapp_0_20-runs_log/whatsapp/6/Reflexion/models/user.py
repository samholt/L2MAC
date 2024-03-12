from dataclasses import dataclass

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
	contacts: list = None

	def update_profile_picture(self, new_picture):
		self.profile_picture = new_picture

	def update_status_message(self, new_message):
		self.status_message = new_message

	def update_privacy_settings(self, new_settings):
		self.privacy_settings = new_settings

	def add_contact(self, contact):
		if self.contacts is None:
			self.contacts = []
		self.contacts.append(contact)

	def remove_contact(self, contact):
		if self.contacts is not None and contact in self.contacts:
			self.contacts.remove(contact)
