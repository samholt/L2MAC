class User:
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.last_seen = None
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = None
		self.blocked_contacts = []
		self.groups = []
		self.online = False

	def sign_up(self, db):
		db[self.email] = self

	def recover_password(self):
		return self.password

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def set_online_status(self, status):
		self.online = status
