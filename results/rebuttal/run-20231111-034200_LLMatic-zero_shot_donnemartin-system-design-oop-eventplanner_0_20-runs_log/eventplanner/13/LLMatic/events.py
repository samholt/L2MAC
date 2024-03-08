class Event:
	def __init__(self):
		self.events = {}

	def create_event(self, event_id, event_type, date, time, theme, color_scheme):
		self.events[event_id] = {
			'type': event_type,
			'date': date,
			'time': time,
			'theme': theme,
			'color_scheme': color_scheme
		}

	def update_event(self, event_id, event_type, date, time, theme, color_scheme):
		if event_id in self.events:
			self.events[event_id] = {
				'type': event_type,
				'date': date,
				'time': time,
				'theme': theme,
				'color_scheme': color_scheme
			}

	def view_event(self, event_id):
		return self.events.get(event_id, 'Event not found')

