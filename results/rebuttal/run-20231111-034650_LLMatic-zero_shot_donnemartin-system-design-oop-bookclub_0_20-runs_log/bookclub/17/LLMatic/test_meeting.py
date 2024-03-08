from meeting import Meeting

def test_schedule_meeting():
	meeting = Meeting()
	assert meeting.schedule_meeting('Test Meeting', 'This is a test meeting', '2022-12-31 12:00:00', ['John Doe', 'Jane Doe']) == 1

def test_get_meeting():
	meeting = Meeting()
	assert meeting.get_meeting(1) == 'Meeting not found'

def test_update_meeting():
	meeting = Meeting()
	assert meeting.update_meeting(1, 'Updated Meeting', 'This is an updated meeting', '2022-12-31 13:00:00', ['John Doe', 'Jane Doe']) == 'Meeting not found'

def test_delete_meeting():
	meeting = Meeting()
	assert meeting.delete_meeting(1) == 'Meeting not found'
