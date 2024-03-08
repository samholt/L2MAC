class User:
	def __init__(self, email, password, profile_picture, status_message, privacy_settings):
		self.email = email
		self.password = password
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings
		self.blocked_users = []
