from datetime import datetime


class Event:
	def __init__(self, event_type, date, time, theme, color_scheme):
		self.event_type = event_type
		self.date = datetime.strptime(date, '%Y-%m-%d')
		self.time = datetime.strptime(time, '%H:%M')
		self.theme = theme
		self.color_scheme = color_scheme

	def update_event(self, event_type=None, date=None, time=None, theme=None, color_scheme=None):
		if event_type:
			self.event_type = event_type
		if date:
			self.date = datetime.strptime(date, '%Y-%m-%d')
		if time:
			self.time = datetime.strptime(time, '%H:%M')
		if theme:
			self.theme = theme
		if color_scheme:
			self.color_scheme = color_scheme

	def view_event(self):
		return {
			'event_type': self.event_type,
			'date': self.date.strftime('%Y-%m-%d'),
			'time': self.time.strftime('%H:%M'),
			'theme': self.theme,
			'color_scheme': self.color_scheme
		}


class EventManagement:
	def __init__(self):
		self.events = []

	def create_event(self, event_type, date, time, theme, color_scheme):
		event = Event(event_type, date, time, theme, color_scheme)
		self.events.append(event)
		return event.view_event()

	def update_event(self, event_index, event_type=None, date=None, time=None, theme=None, color_scheme=None):
		if 0 <= event_index < len(self.events):
			self.events[event_index].update_event(event_type, date, time, theme, color_scheme)
			return self.events[event_index].view_event()
		else:
			return 'Invalid event index'

	def view_events(self):
		return [event.view_event() for event in sorted(self.events, key=lambda x: x.date)]
