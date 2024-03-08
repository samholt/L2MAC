import pytest
from meeting import Meeting

def test_meeting():
	meeting = Meeting('1', '2022-12-31', '12:00')
	assert meeting.get_info() == {'id': '1', 'date': '2022-12-31', 'time': '12:00', 'attendees': []}

	meeting.schedule_meeting('2', '2023-01-01', '13:00')
	assert meeting.get_info() == {'id': '2', 'date': '2023-01-01', 'time': '13:00', 'attendees': []}

	meeting.add_attendee('John')
	assert meeting.get_info() == {'id': '2', 'date': '2023-01-01', 'time': '13:00', 'attendees': ['John']}

	meeting.remove_attendee('John')
	assert meeting.get_info() == {'id': '2', 'date': '2023-01-01', 'time': '13:00', 'attendees': []}
