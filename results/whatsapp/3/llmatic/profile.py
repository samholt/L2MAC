class Profile:
	def __init__(self, user, profile_picture=None, status_message=None, privacy_settings=None):
		self.user = user
		self.profile_picture = profile_picture
		self.status_message = status_message
		self.privacy_settings = privacy_settings if privacy_settings else {}

	def set_profile_picture(self, profile_picture):
		self.profile_picture = profile_picture

	def set_status_message(self, status_message):
		self.status_message = status_message

	def manage_privacy_settings(self, privacy_settings):
		self.privacy_settings = privacy_settings
