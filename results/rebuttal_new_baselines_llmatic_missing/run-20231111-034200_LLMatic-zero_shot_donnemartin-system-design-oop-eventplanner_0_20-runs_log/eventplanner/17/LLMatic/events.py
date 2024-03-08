from datetime import datetime

# Mock database
EVENTS_DB = {}


def create_event(event_id, event_name, event_date, event_details):
	"""Create a new event."""
	if event_id in EVENTS_DB:
		return 'Event already exists.'
	else:
		EVENTS_DB[event_id] = {
			'name': event_name,
			'date': event_date.date(),
			'details': event_details
		}
		return 'Event created successfully.'


def update_event(event_id, event_name=None, event_date=None, event_details=None):
	"""Update an existing event."""
	if event_id not in EVENTS_DB:
		return 'Event does not exist.'
	else:
		if event_name:
			EVENTS_DB[event_id]['name'] = event_name
		if event_date:
			EVENTS_DB[event_id]['date'] = event_date.date()
		if event_details:
			EVENTS_DB[event_id]['details'] = event_details
		return 'Event updated successfully.'


def get_calendar_view():
	"""Provide a calendar view of all events."""
	calendar_view = {}
	for event_id, event in EVENTS_DB.items():
		date = event['date']
		if date not in calendar_view:
			calendar_view[date] = [event_id]
		else:
			calendar_view[date].append(event_id)
	return calendar_view
