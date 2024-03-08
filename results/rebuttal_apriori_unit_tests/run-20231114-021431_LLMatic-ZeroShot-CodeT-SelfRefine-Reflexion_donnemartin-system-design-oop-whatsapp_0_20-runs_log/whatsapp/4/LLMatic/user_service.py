class UserService:
	def __init__(self):
		self.users = {}

	def set_profile(self, user_id, picture_path, status_message):
		if user_id not in self.users:
			self.users[user_id] = {}
		self.users[user_id]['picture'] = picture_path
		self.users[user_id]['status'] = status_message
		return True

	def set_privacy(self, user_id, privacy_settings):
		if user_id not in self.users:
			self.users[user_id] = {}
		self.users[user_id]['privacy'] = privacy_settings
		return True
