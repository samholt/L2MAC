from dataclasses import dataclass

@dataclass
class User:
	id: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None
	blocked_contacts: list = None
	groups: list = None

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def block_contact(self, contact):
		if self.blocked_contacts is None:
			self.blocked_contacts = []
		self.blocked_contacts.append(contact)

	def unblock_contact(self, contact):
		if self.blocked_contacts and contact in self.blocked_contacts:
			self.blocked_contacts.remove(contact)

	def add_group(self, group):
		if self.groups is None:
			self.groups = []
		self.groups.append(group)

	def remove_group(self, group):
		if self.groups and group in self.groups:
			self.groups.remove(group)
