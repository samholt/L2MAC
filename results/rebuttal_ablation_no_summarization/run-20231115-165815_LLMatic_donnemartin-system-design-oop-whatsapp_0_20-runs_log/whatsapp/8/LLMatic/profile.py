class Profile:
	def __init__(self):
		self.profile_picture = None
		self.status_message = ''
		self.privacy_settings = {}

	def set_profile_picture(self, image_file):
		self.profile_picture = image_file

	def set_status_message(self, message):
		self.status_message = message

	def configure_privacy_settings(self, settings):
		self.privacy_settings = settings

	def view_profile(self):
		return {'profile_picture': self.profile_picture, 'status_message': self.status_message, 'privacy_settings': self.privacy_settings}

	def edit_profile(self):
		pass
