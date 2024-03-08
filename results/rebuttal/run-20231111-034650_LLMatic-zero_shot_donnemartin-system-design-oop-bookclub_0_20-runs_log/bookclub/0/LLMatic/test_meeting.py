import datetime
import pytz
from meeting import Meeting


def test_meeting():
	meeting = Meeting(datetime.date.today(), datetime.time(12, 0), 'Book Club', ['John', 'Jane'])
	assert meeting.date == datetime.date.today()
	assert meeting.time == datetime.time(12, 0)
	assert meeting.book_club == 'Book Club'
	assert meeting.attendees == ['John', 'Jane']

	meeting.schedule_meeting(datetime.date.today(), datetime.time(13, 0), 'Book Club', ['John', 'Jane', 'Doe'])
	assert meeting.date == datetime.date.today()
	assert meeting.time == datetime.time(13, 0)
	assert meeting.book_club == 'Book Club'
	assert meeting.attendees == ['John', 'Jane', 'Doe']

	meeting.update_meeting(time=datetime.time(14, 0))
	assert meeting.time == datetime.time(14, 0)

	meeting.send_reminders()

	class MockCalendarApp:
		def schedule_event(self, date, time, event, attendees):
			pass

	mock_calendar_app = MockCalendarApp()
	meeting.integrate_with_calendar(mock_calendar_app)
