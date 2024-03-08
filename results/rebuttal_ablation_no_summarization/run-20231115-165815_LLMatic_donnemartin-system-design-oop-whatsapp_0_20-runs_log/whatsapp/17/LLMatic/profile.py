class Profile:
	def __init__(self, username):
		self.username = username
		self.profile_picture = None
		self.status_message = None
		self.privacy_settings = {'view_profile_picture': 'everyone', 'view_status_message': 'everyone'}

	def set_profile_picture(self, picture):
		self.profile_picture = picture

	def set_status_message(self, message):
		self.status_message = message

	def set_privacy_settings(self, setting, value):
		self.privacy_settings[setting] = value
