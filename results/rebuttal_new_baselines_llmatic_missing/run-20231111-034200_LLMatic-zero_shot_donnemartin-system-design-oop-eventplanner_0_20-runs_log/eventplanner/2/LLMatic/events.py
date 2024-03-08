class Event:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event):
		self.events[event_id] = event
		return self.events

	def update_event(self, event_id, event):
		if event_id in self.events:
			self.events[event_id] = event
		return self.events

	def get_event(self, event_id):
		return self.events.get(event_id, 'Event not found')

	def get_all_events(self):
		return self.events
