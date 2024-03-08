class Event:
	def __init__(self, event_type, date, time, theme, color_scheme):
		self.event_type = event_type
		self.date = date
		self.time = time
		self.theme = theme
		self.color_scheme = color_scheme

	def create_event(self):
		return {'event_type': self.event_type, 'date': self.date, 'time': self.time, 'theme': self.theme, 'color_scheme': self.color_scheme}

	def update_event(self, event_type=None, date=None, time=None, theme=None, color_scheme=None):
		if event_type:
			self.event_type = event_type
		if date:
			self.date = date
		if time:
			self.time = time
		if theme:
			self.theme = theme
		if color_scheme:
			self.color_scheme = color_scheme
		return {'event_type': self.event_type, 'date': self.date, 'time': self.time, 'theme': self.theme, 'color_scheme': self.color_scheme}

	def view_event(self):
		return {'event_type': self.event_type, 'date': self.date, 'time': self.time, 'theme': self.theme, 'color_scheme': self.color_scheme}
