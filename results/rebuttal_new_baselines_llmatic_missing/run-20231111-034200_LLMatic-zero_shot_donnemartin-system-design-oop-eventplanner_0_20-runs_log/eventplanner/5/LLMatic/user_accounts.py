class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {}
		self.event_preferences = {}

	def create_profile(self, profile):
		self.profile = profile

	def update_profile(self, profile):
		self.profile.update(profile)

	def get_profile(self):
		return self.profile

	def set_event_preferences(self, preferences):
		self.event_preferences = preferences

	def get_event_preferences(self):
		return self.event_preferences
