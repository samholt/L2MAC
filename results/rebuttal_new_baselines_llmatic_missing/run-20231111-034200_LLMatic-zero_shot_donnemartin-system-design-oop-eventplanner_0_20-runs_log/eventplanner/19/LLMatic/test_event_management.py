import pytest
from event_management import EventManagement

def test_create_event():
	em = EventManagement()
	event = em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	assert event == {'event_type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}

def test_update_event():
	em = EventManagement()
	em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	event = em.update_event('1', theme='Marvel', color_scheme='Red')
	assert event == {'event_type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Marvel', 'color_scheme': 'Red'}

def test_view_calendar():
	em = EventManagement()
	em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	calendar = em.view_calendar()
	assert calendar == {'1': {'event_type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Disney', 'color_scheme': 'Blue'}}
