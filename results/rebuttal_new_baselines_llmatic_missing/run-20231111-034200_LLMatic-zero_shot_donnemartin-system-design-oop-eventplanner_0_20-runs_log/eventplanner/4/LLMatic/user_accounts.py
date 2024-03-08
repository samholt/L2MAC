class User:
	def __init__(self, name, preferences, events):
		self.name = name
		self.preferences = preferences
		self.events = events

	def update_profile(self, name=None, preferences=None, events=None):
		if name is not None:
			self.name = name
		if preferences is not None:
			self.preferences = preferences
		if events is not None:
			self.events = events

# Mock database
users = {}

