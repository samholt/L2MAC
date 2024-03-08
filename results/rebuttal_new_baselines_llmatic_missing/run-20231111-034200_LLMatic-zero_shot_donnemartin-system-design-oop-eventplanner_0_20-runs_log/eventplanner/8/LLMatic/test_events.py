from events import Event
from database import Database

def test_event_creation():
	db = Database()
	event = Event(1, 'Test Event', '2022-12-31', 'Test Location')
	db.add_event(event)
	assert db.get_event(1) == event.view_event()

def test_event_update():
	db = Database()
	event = Event(1, 'Test Event', '2022-12-31', 'Test Location')
	db.add_event(event)
	event.update_event('Updated Event', '2023-01-01', 'Updated Location')
	db.update_event(1, 'Updated Event', '2023-01-01', 'Updated Location')
	assert db.get_event(1) == event.view_event()

def test_view_all_events():
	db = Database()
	event1 = Event(1, 'Test Event 1', '2022-12-31', 'Test Location 1')
	event2 = Event(2, 'Test Event 2', '2023-01-01', 'Test Location 2')
	db.add_event(event1)
	db.add_event(event2)
	assert db.get_all_events() == {1: event1.view_event(), 2: event2.view_event()}
