class Meeting:
	def __init__(self, id, date, time, book_club):
		self.id = id
		self.date = date
		self.time = time
		self.book_club = book_club

	def schedule_meeting(self, date, time):
		self.date = date
		self.time = time

	def send_reminders(self):
		for member in self.book_club.members:
			member.notify('Reminder for the upcoming meeting on ' + self.date + ' at ' + self.time)
