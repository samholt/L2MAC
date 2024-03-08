class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.profile = {}
		self.events = {'past': [], 'upcoming': []}

	def create_profile(self, profile):
		self.profile = profile

	def customize_profile(self, profile):
		self.profile.update(profile)

	def save_event(self, event, event_type):
		self.events[event_type].append(event)

	def get_events(self, event_type):
		return self.events[event_type]
