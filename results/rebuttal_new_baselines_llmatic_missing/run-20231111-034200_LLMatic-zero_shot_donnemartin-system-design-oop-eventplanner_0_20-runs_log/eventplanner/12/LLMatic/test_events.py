import events

def test_create_event():
	event = events.create_event('1', 'Wedding', '2022-12-12', '12:00', 'Classic', 'White')
	assert event.event_id == '1'
	assert event.event_type == 'Wedding'
	assert event.date == '2022-12-12'
	assert event.time == '12:00'
	assert event.theme == 'Classic'
	assert event.color_scheme == 'White'

def test_update_event():
	event = events.update_event('1', 'Birthday', '2022-12-13', '13:00', 'Fun', 'Blue')
	assert event.event_id == '1'
	assert event.event_type == 'Birthday'
	assert event.date == '2022-12-13'
	assert event.time == '13:00'
	assert event.theme == 'Fun'
	assert event.color_scheme == 'Blue'

def test_view_event():
	event = events.view_event('1')
	assert event.event_id == '1'
	assert event.event_type == 'Birthday'
	assert event.date == '2022-12-13'
	assert event.time == '13:00'
	assert event.theme == 'Fun'
	assert event.color_scheme == 'Blue'
