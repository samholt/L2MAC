events = {}

def create_event(data):
	event_id = len(events) + 1
	events[event_id] = data


def update_event(event_id, data):
	events[event_id] = data


def get_events():
	return events
