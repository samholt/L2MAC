class Event:
	def __init__(self, event_type, date, time, theme, color_scheme):
		self.event_type = event_type
		self.date = date
		self.time = time
		self.theme = theme
		self.color_scheme = color_scheme


class EventManagement:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event):
		self.events[event_id] = event

	def update_event(self, event_id, event):
		self.events[event_id] = event

	def view_event(self, event_id):
		return self.events.get(event_id, 'Event not found')

