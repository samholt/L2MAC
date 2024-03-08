class Meeting:
	def __init__(self, date, time, book):
		self.date = date
		self.time = time
		self.book = book
		self.attendees = []

	def schedule_meeting(self, date, time, book):
		self.date = date
		self.time = time
		self.book = book

	def add_attendee(self, attendee):
		self.attendees.append(attendee)
