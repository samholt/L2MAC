class EventManagement:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event_type, date, time, theme=None, color_scheme=None):
		self.events[event_id] = {
			'event_type': event_type,
			'date': date,
			'time': time,
			'theme': theme,
			'color_scheme': color_scheme
		}
		return self.events[event_id]

	def update_event(self, event_id, **kwargs):
		if event_id in self.events:
			for key, value in kwargs.items():
				if key in self.events[event_id]:
					self.events[event_id][key] = value
			return self.events[event_id]
		else:
			return 'Event not found'

	def view_calendar(self):
		return self.events
