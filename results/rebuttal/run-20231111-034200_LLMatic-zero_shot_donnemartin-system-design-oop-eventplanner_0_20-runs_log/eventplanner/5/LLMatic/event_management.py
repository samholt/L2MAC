from datetime import datetime


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

	def create_event(self, event_id, event_type, date, time, theme, color_scheme):
		new_event = Event(event_type, date, time, theme, color_scheme)
		self.events[event_id] = new_event
		return f'Event {event_id} created successfully.'

	def update_event(self, event_id, event_type=None, date=None, time=None, theme=None, color_scheme=None):
		if event_id not in self.events:
			return f'Event {event_id} does not exist.'
		if event_type:
			self.events[event_id].event_type = event_type
		if date:
			self.events[event_id].date = date
		if time:
			self.events[event_id].time = time
		if theme:
			self.events[event_id].theme = theme
		if color_scheme:
			self.events[event_id].color_scheme = color_scheme
		return f'Event {event_id} updated successfully.'

	def view_events(self):
		for event_id, event in self.events.items():
			print(f'Event ID: {event_id}')
			print(f'Event Type: {event.event_type}')
			print(f'Date: {event.date}')
			print(f'Time: {event.time}')
			print(f'Theme: {event.theme}')
			print(f'Color Scheme: {event.color_scheme}')
			print('\n')

