from event_management import EventManagement
from datetime import datetime


def test_event_creation():
	em = EventManagement()
	event = em.create_event('Birthday', '2022-12-31', '18:00', 'Party', 'Blue')
	assert event.event_type == 'Birthday'
	assert event.date == datetime.strptime('2022-12-31', '%Y-%m-%d')
	assert event.time == datetime.strptime('18:00', '%H:%M')
	assert event.theme == 'Party'
	assert event.color_scheme == 'Blue'


def test_event_update():
	em = EventManagement()
	event = em.create_event('Birthday', '2022-12-31', '18:00', 'Party', 'Blue')
	em.update_event(event, new_event_type='Wedding', new_date='2023-01-01', new_time='19:00', new_theme='Celebration', new_color_scheme='Red')
	assert event.event_type == 'Wedding'
	assert event.date == datetime.strptime('2023-01-01', '%Y-%m-%d')
	assert event.time == datetime.strptime('19:00', '%H:%M')
	assert event.theme == 'Celebration'
	assert event.color_scheme == 'Red'


def test_view_events():
	em = EventManagement()
	em.create_event('Birthday', '2022-12-31', '18:00', 'Party', 'Blue')
	em.create_event('Wedding', '2023-01-01', '19:00', 'Celebration', 'Red')
	events = em.view_events()
	assert events[0].event_type == 'Birthday'
	assert events[1].event_type == 'Wedding'

