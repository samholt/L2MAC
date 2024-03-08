class UserService:
	def __init__(self):
		self.user_profiles = {}
		self.user_privacy = {}

	def set_profile(self, user_id, picture_path, status_message):
		self.user_profiles[user_id] = {'picture_path': picture_path, 'status_message': status_message}
		return True

	def set_privacy(self, user_id, privacy_settings):
		self.user_privacy[user_id] = privacy_settings
		return True
