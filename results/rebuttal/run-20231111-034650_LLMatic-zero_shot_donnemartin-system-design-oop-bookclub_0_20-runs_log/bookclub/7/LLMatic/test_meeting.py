import pytest
from meeting import Meeting

def test_schedule_meeting():
	meeting = Meeting()
	meeting.schedule_meeting('1', 'Meeting 1')
	assert meeting.meetings['1'] == 'Meeting 1'

def test_send_reminder():
	meeting = Meeting()
	meeting.schedule_meeting('1', 'Meeting 1')
	assert meeting.send_reminder('1') == 'Reminder sent for meeting: Meeting 1'

def test_integrate_with_calendar():
	meeting = Meeting()
	meeting.schedule_meeting('1', 'Meeting 1')
	assert meeting.integrate_with_calendar('1', 'Google Calendar') == 'Meeting: Meeting 1 integrated with Google Calendar'
