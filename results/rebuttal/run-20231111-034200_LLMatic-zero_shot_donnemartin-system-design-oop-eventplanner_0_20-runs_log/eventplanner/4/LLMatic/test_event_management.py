import pytest
import event_management

def test_import():
	assert event_management is not None

def test_event_creation():
	event = event_management.Event('Birthday', '2022-12-12', '18:00', 'Casual', 'Blue')
	event_management.create_event('1', event)
	assert event_management.view_event('1') == event

def test_event_update():
	event = event_management.Event('Wedding', '2023-01-01', '12:00', 'Formal', 'White')
	event_management.update_event('1', event)
	assert event_management.view_event('1') == event

