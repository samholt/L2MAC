import datetime

class User:
	def __init__(self, email, password, profile_picture=None, status_message=None, privacy_settings=None):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings if privacy_settings else {}
		self.blocked = False
		self.last_online = datetime.datetime.now()
		self.queued_messages = []

	def update_profile(self, profile_picture=None, status_message=None, privacy_settings=None):
		if profile_picture:
			self.profile_picture = profile_picture
		if status_message:
			self.status_message = status_message
		if privacy_settings:
			self.privacy_settings = privacy_settings

	def block(self):
		self.blocked = True

	def unblock(self):
		self.blocked = False

	def update_last_online(self):
		self.last_online = datetime.datetime.now()

	def queue_message(self, message):
		self.queued_messages.append(message)

	def send_queued_messages(self):
		for message in self.queued_messages:
			# Assuming send_message is a function that sends a message
			# send_message(message)
			pass
		self.queued_messages = []
