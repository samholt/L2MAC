import pytest
from meeting import Meeting

def test_schedule_meeting():
	meeting = Meeting('2022-12-01', '18:00', 'Book Title')
	meeting.schedule_meeting('2022-12-02', '19:00', 'New Book Title')
	assert meeting.date == '2022-12-02'
	assert meeting.time == '19:00'
	assert meeting.book == 'New Book Title'

def test_add_attendee():
	meeting = Meeting('2022-12-01', '18:00', 'Book Title')
	meeting.add_attendee('John Doe')
	assert 'John Doe' in meeting.attendees
