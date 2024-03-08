import pytest
import meeting


def test_schedule_meeting_missing_data():
	meeting_obj = meeting.Meeting()
	with pytest.raises(ValueError):
		meeting_obj.schedule_meeting('', '')


def test_send_reminder_missing_data():
	meeting_obj = meeting.Meeting()
	with pytest.raises(ValueError):
		meeting_obj.send_reminder('')
