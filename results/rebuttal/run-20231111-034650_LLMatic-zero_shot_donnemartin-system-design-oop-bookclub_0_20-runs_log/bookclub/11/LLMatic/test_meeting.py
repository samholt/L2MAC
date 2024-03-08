import pytest
from meeting import Meeting

def test_schedule_meeting():
	meeting = Meeting()
	message = meeting.schedule_meeting('2022-12-25 18:00', 'Book Club 1', ['User 1', 'User 2'])
	assert message == 'Meeting scheduled successfully'

def test_send_reminders():
	meeting = Meeting()
	meeting.schedule_meeting('2022-12-25 18:00', 'Book Club 1', ['User 1', 'User 2'])
	message = meeting.send_reminders('Book Club 1')
	assert message == 'Reminders sent for all meetings of this book club'
