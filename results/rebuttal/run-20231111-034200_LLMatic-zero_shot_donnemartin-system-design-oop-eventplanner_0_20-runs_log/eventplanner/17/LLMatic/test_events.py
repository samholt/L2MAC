import events
from datetime import datetime

def test_create_event():
	result = events.create_event('1', 'Event 1', datetime.now(), 'Details of Event 1')
	assert result == 'Event created successfully.'

	result = events.create_event('1', 'Event 1', datetime.now(), 'Details of Event 1')
	assert result == 'Event already exists.'


def test_update_event():
	result = events.update_event('1', 'Updated Event 1', datetime.now(), 'Updated details of Event 1')
	assert result == 'Event updated successfully.'

	result = events.update_event('2')
	assert result == 'Event does not exist.'


def test_get_calendar_view():
	calendar_view = events.get_calendar_view()
	assert isinstance(calendar_view, dict)
	assert '1' in calendar_view[datetime.now().date()]
