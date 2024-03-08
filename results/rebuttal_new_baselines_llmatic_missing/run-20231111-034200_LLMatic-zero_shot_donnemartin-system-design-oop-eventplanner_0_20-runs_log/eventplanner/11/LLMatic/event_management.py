class EventManagement:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event_details):
		if event_id in self.events:
			return 'Event already exists'
		self.events[event_id] = event_details
		return 'Event created successfully'

	def update_event(self, event_id, updated_details):
		if event_id not in self.events:
			return 'Event does not exist'
		self.events[event_id].update(updated_details)
		return 'Event updated successfully'

	def get_calendar_view(self):
		return self.events
