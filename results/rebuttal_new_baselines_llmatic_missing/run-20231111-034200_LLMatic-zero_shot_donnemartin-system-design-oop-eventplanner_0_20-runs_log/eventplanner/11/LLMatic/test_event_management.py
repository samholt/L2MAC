import pytest
from event_management import EventManagement

def test_create_event():
	em = EventManagement()
	assert em.create_event('1', {'name': 'Birthday Party', 'date': '2022-12-12'}) == 'Event created successfully'
	assert em.create_event('1', {'name': 'Anniversary', 'date': '2022-12-13'}) == 'Event already exists'

def test_update_event():
	em = EventManagement()
	em.create_event('1', {'name': 'Birthday Party', 'date': '2022-12-12'})
	assert em.update_event('1', {'name': 'Anniversary'}) == 'Event updated successfully'
	assert em.update_event('2', {'name': 'Wedding'}) == 'Event does not exist'

def test_get_calendar_view():
	em = EventManagement()
	em.create_event('1', {'name': 'Birthday Party', 'date': '2022-12-12'})
	assert em.get_calendar_view() == {'1': {'name': 'Birthday Party', 'date': '2022-12-12'}}
