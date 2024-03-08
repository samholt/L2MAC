import hashlib


class User:
	def __init__(self, email, password):
		self.email = email
		self.password = self.hash_password(password)
		self.last_login = None
		self.is_active = False
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = {'show_details': True, 'show_last_seen': True}
		self.status = []

	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode()).hexdigest()

	def register(self):
		# Add user to database
		pass

	def login(self):
		# Authenticate user and update last_login
		pass

	def logout(self):
		# Set is_active to False
		self.is_active = False

	def forgot_password(self):
		# Reset user's password
		pass

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, settings):
		self.privacy_settings = settings
