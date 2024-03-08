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
		self.connectivity = True

	def sign_up(self, db):
		if self.email in db:
			return 'Email already exists'
		else:
			db[self.email] = self
			return 'User created successfully'

	def recover_password(self):
		return 'Password recovery email sent'

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings

	def set_connectivity(self, status):
		self.connectivity = status
