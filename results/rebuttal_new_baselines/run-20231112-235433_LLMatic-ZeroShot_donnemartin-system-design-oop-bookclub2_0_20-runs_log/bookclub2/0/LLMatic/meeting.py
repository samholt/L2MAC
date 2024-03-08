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
		for attendee in self.attendees:
			print(f'Reminder sent to {attendee}')
