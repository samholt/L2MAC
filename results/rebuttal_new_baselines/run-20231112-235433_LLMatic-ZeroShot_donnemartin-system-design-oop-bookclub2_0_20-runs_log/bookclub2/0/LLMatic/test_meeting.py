from meeting import Meeting

def test_meeting():
	meeting = Meeting('2022-12-31', '12:00', 'Book Club 1', ['User 1', 'User 2'])
	assert meeting.date == '2022-12-31'
	assert meeting.time == '12:00'
	assert meeting.book_club == 'Book Club 1'
	assert meeting.attendees == ['User 1', 'User 2']

	meeting.schedule_meeting('2023-01-01', '13:00', 'Book Club 2', ['User 3', 'User 4'])
	assert meeting.date == '2023-01-01'
	assert meeting.time == '13:00'
	assert meeting.book_club == 'Book Club 2'
	assert meeting.attendees == ['User 3', 'User 4']

	meeting.update_meeting(date='2023-01-02', time='14:00')
	assert meeting.date == '2023-01-02'
	assert meeting.time == '14:00'

	meeting.send_reminders()
