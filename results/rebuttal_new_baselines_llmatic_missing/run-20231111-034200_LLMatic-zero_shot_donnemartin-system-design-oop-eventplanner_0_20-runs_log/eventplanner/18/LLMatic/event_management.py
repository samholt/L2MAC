from datetime import datetime


class Event:
	def __init__(self, event_type, date, time, theme, color_scheme):
		self.event_type = event_type
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self.time = datetime.strptime(time, '%H:%M')
		self.theme = theme
		self.color_scheme = color_scheme


class EventManagement:
	def __init__(self):
		self.events = []

	def create_event(self, event_type, date, time, theme, color_scheme):
		event = Event(event_type, date, time, theme, color_scheme)
		self.events.append(event)
		return event

	def update_event(self, event, new_event_type=None, new_date=None, new_time=None, new_theme=None, new_color_scheme=None):
		if new_event_type:
			event.event_type = new_event_type
		if new_date:
			event.date = datetime.strptime(new_date, '%Y-%m-%d')
		if new_time:
			event.time = datetime.strptime(new_time, '%H:%M')
		if new_theme:
			event.theme = new_theme
		if new_color_scheme:
			event.color_scheme = new_color_scheme
		return event

	def view_events(self):
		return sorted(self.events, key=lambda event: event.date)

