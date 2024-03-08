import pytest
from meeting import Meeting

def test_schedule_new_meeting():
	meeting = Meeting('2022-12-31', '10:00', 'Book Club 1')
	assert meeting.schedule_new_meeting('2023-01-01', '11:00') == 'Meeting has been scheduled on 2023-01-01 at 11:00 for Book Club 1'

def test_send_reminders():
	meeting = Meeting('2022-12-31', '10:00', 'Book Club 1')
	members = ['member1', 'member2', 'member3']
	meeting.send_reminders(members)
	# As the send_reminders method does not return anything, we just check if it runs without errors
