class User:
	def __init__(self, user_id, name, contact_info, preferences):
		self.user_id = user_id
		self.name = name
		self.contact_info = contact_info
		self.preferences = preferences
		self.past_events = []
		self.upcoming_events = []

	def create_profile(self, name, contact_info, preferences):
		self.name = name
		self.contact_info = contact_info
		self.preferences = preferences

	def update_profile(self, name=None, contact_info=None, preferences=None):
		if name:
			self.name = name
		if contact_info:
			self.contact_info = contact_info
		if preferences:
			self.preferences = preferences

	def view_profile(self):
		return {
			'user_id': self.user_id,
			'name': self.name,
			'contact_info': self.contact_info,
			'preferences': self.preferences,
			'past_events': self.past_events,
			'upcoming_events': self.upcoming_events
		}

	def save_event(self, event, is_upcoming=True):
		if is_upcoming:
			self.upcoming_events.append(event)
		else:
			self.past_events.append(event)

	def get_past_events(self):
		return self.past_events

	def get_upcoming_events(self):
		return self.upcoming_events
