import event_management

def test_create_event():
	event_data = {'name': 'Test Event', 'date': '2022-12-31', 'location': 'Test Location'}
	event_management.create_event(event_data)
	assert event_management.events[1] == event_data

def test_update_event():
	event_data = {'name': 'Updated Event', 'date': '2022-12-31', 'location': 'Test Location'}
	event_management.update_event(1, event_data)
	assert event_management.events[1] == event_data

def test_get_events():
	assert event_management.get_events() == event_management.events
