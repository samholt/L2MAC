import pytest
from events import Event

def test_create_event():
	event = Event()
	assert event.create_event('1', {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'}) == 'Event created successfully'
	assert event.create_event('1', {'name': 'Anniversary Party', 'date': '2022-02-01', 'location': 'Restaurant'}) == 'Event already exists'

def test_update_event():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'})
	assert event.update_event('1', {'name': 'Anniversary Party', 'date': '2022-02-01', 'location': 'Restaurant'}) == 'Event updated successfully'
	assert event.update_event('2', {'name': 'Wedding Party', 'date': '2022-03-01', 'location': 'Beach'}) == 'Event does not exist'

def test_view_event():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'})
	assert event.view_event('1') == {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'}
	assert event.view_event('2') == 'Event does not exist'

def test_view_all_events():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'})
	event.create_event('2', {'name': 'Anniversary Party', 'date': '2022-02-01', 'location': 'Restaurant'})
	assert event.view_all_events() == {'1': {'name': 'Birthday Party', 'date': '2022-01-01', 'location': 'Home'}, '2': {'name': 'Anniversary Party', 'date': '2022-02-01', 'location': 'Restaurant'}}
