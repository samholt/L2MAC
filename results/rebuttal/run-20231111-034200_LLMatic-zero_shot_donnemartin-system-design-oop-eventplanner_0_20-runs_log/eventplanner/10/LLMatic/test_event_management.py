import pytest
from event_management import Event, EventManagement


def test_event_creation():
	event_management = EventManagement()
	event = Event('Wedding', '2022-12-12', '18:00', 'Classic', 'White and Gold')
	event_management.create_event('1', event)
	assert event_management.view_event('1') == event


def test_event_update():
	event_management = EventManagement()
	event = Event('Wedding', '2022-12-12', '18:00', 'Classic', 'White and Gold')
	event_management.create_event('1', event)
	updated_event = Event('Wedding', '2022-12-13', '18:00', 'Classic', 'White and Gold')
	event_management.update_event('1', updated_event)
	assert event_management.view_event('1') == updated_event

