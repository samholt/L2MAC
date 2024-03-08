class Event:
	def __init__(self, event_id, event_type, date, time, theme, color_scheme):
		self.event_id = event_id
		self.event_type = event_type
		self.date = date
		self.time = time
		self.theme = theme
		self.color_scheme = color_scheme

# Mock database
events_db = {}

def create_event(event_id, event_type, date, time, theme, color_scheme):
	event = Event(event_id, event_type, date, time, theme, color_scheme)
	events_db[event_id] = event
	return event

def update_event(event_id, event_type, date, time, theme, color_scheme):
	event = events_db.get(event_id)
	if event:
		event.event_type = event_type
		event.date = date
		event.time = time
		event.theme = theme
		event.color_scheme = color_scheme
	return event

def view_event(event_id):
	return events_db.get(event_id)
