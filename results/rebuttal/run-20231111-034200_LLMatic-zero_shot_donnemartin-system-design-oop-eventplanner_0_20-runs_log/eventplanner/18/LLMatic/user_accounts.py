class User:
	def __init__(self, name, preferences, event_history):
		self.name = name
		self.preferences = preferences
		self.event_history = event_history

	def create_profile(self, name, preferences):
		self.name = name
		self.preferences = preferences
		self.event_history = []

	def update_profile(self, name=None, preferences=None):
		if name is not None:
			self.name = name
		if preferences is not None:
			self.preferences = preferences

	def add_event_to_history(self, event):
		self.event_history.append(event)
