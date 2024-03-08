class Event:
	def __init__(self, name, date, location):
		self.name = name
		self.date = date
		self.location = location
		self.customizations = {}

	def customize_event(self, customization):
		self.customizations.update(customization)

	def update_event(self, name=None, date=None, location=None):
		if name:
			self.name = name
		if date:
			self.date = date
		if location:
			self.location = location


class Calendar:
	def __init__(self):
		self.events = {}

	def add_event(self, event):
		self.events[event.name] = event

	def view_calendar(self):
		return self.events
