import pytest
from events import Event

def test_create_event():
	event = Event()
	assert event.create_event('1', {'name': 'Birthday Party'}) == {'1': {'name': 'Birthday Party'}}

def test_update_event():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party'})
	assert event.update_event('1', {'name': 'Anniversary Party'}) == {'1': {'name': 'Anniversary Party'}}

def test_get_event():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party'})
	assert event.get_event('1') == {'name': 'Birthday Party'}

def test_get_all_events():
	event = Event()
	event.create_event('1', {'name': 'Birthday Party'})
	event.create_event('2', {'name': 'Anniversary Party'})
	assert event.get_all_events() == {'1': {'name': 'Birthday Party'}, '2': {'name': 'Anniversary Party'}}
