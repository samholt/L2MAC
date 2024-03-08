class User:
	def __init__(self, username, password, profile):
		self.username = username
		self.password = password
		self.profile = profile
		self.events = []

	def customize_profile(self, profile):
		self.profile = profile

	def save_event(self, event):
		self.events.append(event)

	def get_events(self):
		return self.events

