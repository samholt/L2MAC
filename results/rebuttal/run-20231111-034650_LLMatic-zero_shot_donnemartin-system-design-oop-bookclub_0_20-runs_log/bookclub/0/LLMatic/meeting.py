import datetime
import pytz


class Meeting:
	def __init__(self, date, time, book_club, attendees):
		self.date = date
		self.time = time
		self.book_club = book_club
		self.attendees = attendees

	def schedule_meeting(self, date, time, book_club, attendees):
		self.date = date
		self.time = time
		self.book_club = book_club
		self.attendees = attendees

	def update_meeting(self, date=None, time=None, book_club=None, attendees=None):
		if date:
			self.date = date
		if time:
			self.time = time
		if book_club:
			self.book_club = book_club
		if attendees:
			self.attendees = attendees

	def send_reminders(self):
		current_time = datetime.datetime.now(pytz.timezone('UTC'))
		meeting_time = datetime.datetime.combine(self.date, self.time, pytz.timezone('UTC'))
		if (meeting_time - current_time).total_seconds() <= 3600:
			for attendee in self.attendees:
				print(f'Sending reminder to {attendee}')

	def integrate_with_calendar(self, calendar_app):
		calendar_app.schedule_event(self.date, self.time, self.book_club, self.attendees)
