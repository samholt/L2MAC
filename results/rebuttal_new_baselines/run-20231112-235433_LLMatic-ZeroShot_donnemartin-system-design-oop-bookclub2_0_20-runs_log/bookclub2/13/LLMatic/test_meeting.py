import pytest
from meeting import Meeting

def test_meeting():
	meeting = Meeting('2022-12-31', '12:00', ['John', 'Jane'], ['Reminder 1', 'Reminder 2'])
	assert meeting.date == '2022-12-31'
	assert meeting.time == '12:00'
	assert meeting.attendees == ['John', 'Jane']
	assert meeting.reminders == ['Reminder 1', 'Reminder 2']

	meeting.schedule_meeting('2023-01-01', '13:00', ['John', 'Jane', 'Doe'])
	assert meeting.date == '2023-01-01'
	assert meeting.time == '13:00'
	assert meeting.attendees == ['John', 'Jane', 'Doe']

	meeting.update_meeting(date='2023-01-02', time='14:00')
	assert meeting.date == '2023-01-02'
	assert meeting.time == '14:00'

	meeting.send_reminders()
