class User:
	def __init__(self, name, preferences, events):
		self.name = name
		self.preferences = preferences
		self.events = events

	def create_profile(self, name, preferences):
		self.name = name
		self.preferences = preferences

	def update_profile(self, name, preferences):
		self.name = name
		self.preferences = preferences

	def save_event(self, event):
		self.events.append(event)

	def get_events(self):
		return self.events
