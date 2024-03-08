import pytest
import event_management

def test_create_event():
	event_data = {'name': 'Test Event', 'date': '2022-12-31', 'location': 'Test Location'}
	event_management.create_event(event_data)
	events = event_management.get_events()
	assert events[0] == event_data

def test_update_event():
	event_data = {'name': 'Updated Event', 'date': '2022-12-31', 'location': 'Updated Location'}
	event_management.update_event(0, event_data)
	events = event_management.get_events()
	assert events[0]['name'] == event_data['name']
	assert events[0]['date'] == event_data['date']
	assert events[0]['location'] == event_data['location']
