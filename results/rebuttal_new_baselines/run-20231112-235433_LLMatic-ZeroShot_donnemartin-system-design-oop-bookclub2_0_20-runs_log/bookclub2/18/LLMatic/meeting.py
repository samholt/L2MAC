class Meeting:
	def __init__(self, date, time, book_club):
		self.date = date
		self.time = time
		self.book_club = book_club

	def schedule_new_meeting(self, date, time):
		self.date = date
		self.time = time
		return f'Meeting has been scheduled on {self.date} at {self.time} for {self.book_club}'

	def send_reminders(self, members):
		for member in members:
			print(f'Reminder: Meeting for {self.book_club} on {self.date} at {self.time} has been sent to {member}')
