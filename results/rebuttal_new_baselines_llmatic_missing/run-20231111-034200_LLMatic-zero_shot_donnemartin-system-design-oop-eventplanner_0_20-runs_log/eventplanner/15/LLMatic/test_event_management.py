import event_management

def test_import():
	assert event_management is not None

def test_event_creation():
	event = event_management.Event('Birthday Party', '2022-12-31', 'Home')
	assert event.name == 'Birthday Party'
	assert event.date == '2022-12-31'
	assert event.location == 'Home'

def test_event_customization():
	event = event_management.Event('Birthday Party', '2022-12-31', 'Home')
	event.customize_event({'theme': 'Space'})
	assert event.customizations['theme'] == 'Space'

def test_event_update():
	event = event_management.Event('Birthday Party', '2022-12-31', 'Home')
	event.update_event(name='New Year Party')
	assert event.name == 'New Year Party'

def test_calendar_view():
	calendar = event_management.Calendar()
	event = event_management.Event('Birthday Party', '2022-12-31', 'Home')
	calendar.add_event(event)
	assert 'Birthday Party' in calendar.view_calendar()
