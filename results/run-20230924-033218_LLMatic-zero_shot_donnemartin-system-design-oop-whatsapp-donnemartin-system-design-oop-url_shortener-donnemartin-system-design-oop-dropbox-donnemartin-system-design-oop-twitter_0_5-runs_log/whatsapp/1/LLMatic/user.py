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

	def sign_up(self, db):
		if self.email in db:
			return 'User already exists'
		db[self.email] = self
		return 'User registered successfully'

	def recover_password(self, db):
		if self.email in db:
			return db[self.email].password
		return 'User not found'

	def set_profile_picture(self, picture):
		self.profile_picture = picture
		return 'Profile picture updated successfully'

	def set_status_message(self, message):
		self.status_message = message
		return 'Status message updated successfully'

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings
		return 'Privacy settings updated successfully'
