class UserProfile:
	def __init__(self):
		self.user_profiles = {}

	def set_profile_picture(self, email, picture):
		if email not in self.user_profiles:
			self.user_profiles[email] = {'picture': '', 'status': '', 'privacy': ''}
		self.user_profiles[email]['picture'] = picture

	def set_status_message(self, email, status):
		if email not in self.user_profiles:
			self.user_profiles[email] = {'picture': '', 'status': '', 'privacy': ''}
		self.user_profiles[email]['status'] = status

	def set_privacy_settings(self, email, privacy):
		if email not in self.user_profiles:
			self.user_profiles[email] = {'picture': '', 'status': '', 'privacy': ''}
		self.user_profiles[email]['privacy'] = privacy
