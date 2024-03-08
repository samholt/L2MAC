from event_management import EventManagement


def test_event_creation():
	em = EventManagement()
	assert em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue') == 'Event 1 created successfully.'


def test_event_update():
	em = EventManagement()
	em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	assert em.update_event('1', event_type='Wedding') == 'Event 1 updated successfully.'


def test_view_events():
	em = EventManagement()
	em.create_event('1', 'Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	em.view_events()

