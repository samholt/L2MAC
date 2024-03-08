class Event:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event_details):
		if event_id in self.events:
			return 'Event already exists'
		self.events[event_id] = event_details
		return 'Event created successfully'

	def update_event(self, event_id, event_details):
		if event_id not in self.events:
			return 'Event does not exist'
		self.events[event_id] = event_details
		return 'Event updated successfully'

	def view_event(self, event_id):
		if event_id not in self.events:
			return 'Event does not exist'
		return self.events[event_id]

	def view_all_events(self):
		return self.events
