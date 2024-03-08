class User:
	def __init__(self, name, preferences, events):
		self.name = name
		self.preferences = preferences
		self.events = events

	def create_profile(self, name, preferences):
		self.name = name
		self.preferences = preferences

	def customize_profile(self, name=None, preferences=None):
		if name:
			self.name = name
		if preferences:
			self.preferences = preferences

	def save_event(self, event):
		self.events.append(event)

	def access_event(self, event_id):
		for event in self.events:
			if event == event_id:
				return event

# Mock database
users = {}

