import pytest
from events import Event
from database import Database

def test_event_creation_and_management():
	db = Database()
	event = Event('Birthday', '2022-12-12', '18:00', 'Casual', 'Blue')
	event_data = event.create_event()
	db.add_event('1', event_data)
	assert db.get_event('1') == event_data
	event.update_event(event_type='Wedding')
	updated_event_data = event.view_event()
	db.update_event('1', updated_event_data)
	assert db.get_event('1') == updated_event_data
