import pytest
from meeting import Meeting

def test_schedule_meeting():
	meeting = Meeting()
	meeting.schedule_meeting('book_club_1', 'meeting_1', '2022-12-31 10:00:00')
	assert meeting.meetings['book_club_1']['meeting_1']['time'] == '2022-12-31 10:00:00'

def test_set_reminder():
	meeting = Meeting()
	meeting.schedule_meeting('book_club_1', 'meeting_1', '2022-12-31 10:00:00')
	meeting.set_reminder('book_club_1', 'meeting_1')
	assert meeting.meetings['book_club_1']['meeting_1']['reminder_set'] == True
