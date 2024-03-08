import pytest
from events import Event

def test_event_creation():
	event = Event()
	event.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')
	assert event.view_event('1') == {
		'event_type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Hawaiian',
		'color_scheme': 'Blue and White'
	}

def test_event_update():
	event = Event()
	event.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Hawaiian', 'Blue and White')
	event.update_event('1', time='19:00', theme='Beach')
	assert event.view_event('1') == {
		'event_type': 'Birthday',
		'date': '2022-12-12',
		'time': '19:00',
		'theme': 'Beach',
		'color_scheme': 'Blue and White'
	}
