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

	def sign_up(self, email, password):
		# Check if email is already in use
		if email in users_db:
			return 'Email already in use'
		else:
			# Add user to the database
			users_db[email] = self
			return 'User created successfully'

	def recover_password(self, email):
		# Send a password recovery email to the user's email address
		return 'Password recovery email sent'

	def set_profile_picture(self, picture):
		# Update the user's profile picture
		self.profile_picture = picture

	def set_status_message(self, message):
		# Update the user's status message
		self.status_message = message

	def set_privacy_settings(self, settings):
		# Update the user's privacy settings
		self.privacy_settings = settings

	def set_online_status(self, status):
		self.online = status

# Mock database
users_db = {}
