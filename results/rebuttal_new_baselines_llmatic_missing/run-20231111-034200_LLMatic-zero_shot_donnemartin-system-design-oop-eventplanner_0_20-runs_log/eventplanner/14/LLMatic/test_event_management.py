from event_management import EventManagement


def test_event_creation():
	em = EventManagement()
	event = em.create_event('Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	assert event == {
		'event_type': 'Birthday',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Disney',
		'color_scheme': 'Blue'
	}


def test_event_update():
	em = EventManagement()
	em.create_event('Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	event = em.update_event(0, event_type='Wedding')
	assert event == {
		'event_type': 'Wedding',
		'date': '2022-12-12',
		'time': '18:00',
		'theme': 'Disney',
		'color_scheme': 'Blue'
	}


def test_view_events():
	em = EventManagement()
	em.create_event('Birthday', '2022-12-12', '18:00', 'Disney', 'Blue')
	em.create_event('Wedding', '2022-12-11', '18:00', 'Classic', 'White')
	events = em.view_events()
	assert events == [
		{
			'event_type': 'Wedding',
			'date': '2022-12-11',
			'time': '18:00',
			'theme': 'Classic',
			'color_scheme': 'White'
		},
		{
			'event_type': 'Birthday',
			'date': '2022-12-12',
			'time': '18:00',
			'theme': 'Disney',
			'color_scheme': 'Blue'
		}
	]
