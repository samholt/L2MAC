class Event:
	def __init__(self, event_type, date, time, theme, color_scheme):
		self.event_type = event_type
		self.date = date
		self.time = time
		self.theme = theme
		self.color_scheme = color_scheme

mock_db = {}

def create_event(event_id, event):
	mock_db[event_id] = event

def update_event(event_id, event):
	mock_db[event_id] = event

def view_event(event_id):
	return mock_db.get(event_id, 'Event not found')

