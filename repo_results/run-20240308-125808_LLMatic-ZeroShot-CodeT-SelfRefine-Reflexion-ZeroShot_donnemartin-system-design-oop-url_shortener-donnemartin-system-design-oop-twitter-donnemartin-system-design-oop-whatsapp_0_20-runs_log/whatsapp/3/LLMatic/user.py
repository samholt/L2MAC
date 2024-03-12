from contact import Contact
from datetime import datetime, timedelta

class User:
	def __init__(self, email, password, profile_picture=None, status_message=None, privacy_settings=None):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings
		self.contacts = {}
		self.statuses = {}
		self.is_online = False
		self.queue = []

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def get_profile_picture(self):
		return self.profile_picture

	def set_status_message(self, status_message):
		self.status_message = status_message

	def get_status_message(self):
		return self.status_message

	def set_privacy_settings(self, privacy_settings):
		self.privacy_settings = privacy_settings

	def get_privacy_settings(self):
		return self.privacy_settings

	def add_contact(self, email):
		self.contacts[email] = Contact(email)

	def get_contact(self, email):
		return self.contacts.get(email, None)

	def block_contact(self, email):
		contact = self.get_contact(email)
		if contact:
			contact.block()

	def unblock_contact(self, email):
		contact = self.get_contact(email)
		if contact:
			contact.unblock()

	def post_status(self, image, visibility):
		status_id = len(self.statuses) + 1
		self.statuses[status_id] = {'image': image, 'posted_at': datetime.now(), 'visibility': visibility}

	def delete_status(self, status_id):
		if status_id in self.statuses:
			del self.statuses[status_id]

	def get_status(self, status_id):
		status = self.statuses.get(status_id)
		if status and datetime.now() - status['posted_at'] <= timedelta(hours=24):
			return status
		return None

	def go_online(self):
		self.is_online = True
		for message in self.queue:
			message.send_queued_messages()
		self.queue = []

	def go_offline(self):
		self.is_online = False
