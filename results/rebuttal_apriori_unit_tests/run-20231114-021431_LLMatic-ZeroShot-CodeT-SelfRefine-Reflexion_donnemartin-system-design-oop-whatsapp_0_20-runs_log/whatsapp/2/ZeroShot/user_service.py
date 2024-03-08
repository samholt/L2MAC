class UserService:
	def __init__(self):
		self.users = {}

	def set_profile(self, user_id, picture_path, status_message):
		self.users[user_id] = {'picture': picture_path, 'status': status_message}
		return True

	def set_privacy(self, user_id, privacy_settings):
		if user_id not in self.users:
			return False
		self.users[user_id]['privacy'] = privacy_settings
		return True
