import pytest
import event_management

def test_create_event():
	event = event_management.Event('Birthday', '2022-12-12', '18:00', 'Casual', 'Blue')
	event_management.create_event('1', event)
	assert event_management.get_event('1') == event


def test_update_event():
	event = event_management.Event('Wedding', '2023-01-01', '12:00', 'Formal', 'White')
	event_management.update_event('1', event)
	assert event_management.get_event('1') == event


def test_get_event():
	event = event_management.get_event('1')
	assert isinstance(event, event_management.Event)


def test_delete_event():
	event_management.delete_event('1')
	assert event_management.get_event('1') == 'Event not found'
