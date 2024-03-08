import pytest
from meeting import Meeting


def test_schedule_meeting():
	meeting = Meeting('1', '2022-01-01', '10:00', 'Book Club 1')
	meeting.schedule_meeting('2022-02-02', '11:00')
	assert meeting.date == '2022-02-02'
	assert meeting.time == '11:00'


def test_update_meeting():
	meeting = Meeting('1', '2022-01-01', '10:00', 'Book Club 1')
	meeting.update_meeting(date='2022-03-03', time='12:00')
	assert meeting.date == '2022-03-03'
	assert meeting.time == '12:00'
