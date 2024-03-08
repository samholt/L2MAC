import pytest
from events import Event

def test_event_creation():
	event_manager = Event()
	event_manager.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')
	assert event_manager.view_event('1') == {
		'type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Hawaiian',
		'color_scheme': 'Blue and White'
	}

def test_event_update():
	event_manager = Event()
	event_manager.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')
	event_manager.update_event('1', 'Wedding', '2022-12-12', '18:00', 'Classic', 'Black and White')
	assert event_manager.view_event('1') == {
		'type': 'Wedding',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Classic',
		'color_scheme': 'Black and White'
	}

