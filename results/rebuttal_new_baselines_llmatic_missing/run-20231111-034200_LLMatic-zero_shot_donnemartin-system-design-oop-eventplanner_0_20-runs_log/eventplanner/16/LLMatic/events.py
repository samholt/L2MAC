class Event:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event_type, date, time, theme, color_scheme):
		self.events[event_id] = {
			'event_type': event_type,
			'date': date,
			'time': time,
			'theme': theme,
			'color_scheme': color_scheme
		}

	def update_event(self, event_id, event_type=None, date=None, time=None, theme=None, color_scheme=None):
		if event_id in self.events:
			if event_type:
				self.events[event_id]['event_type'] = event_type
			if date:
				self.events[event_id]['date'] = date
			if time:
				self.events[event_id]['time'] = time
			if theme:
				self.events[event_id]['theme'] = theme
			if color_scheme:
				self.events[event_id]['color_scheme'] = color_scheme

	def view_event(self, event_id):
		return self.events.get(event_id, 'Event not found.')
