class Meeting:
	def __init__(self, id, date, time, book_club):
		self.id = id
		self.date = date
		self.time = time
		self.book_club = book_club

	def schedule_meeting(self, date, time):
		self.date = date
		self.time = time

	def update_meeting(self, date=None, time=None):
		if date:
			self.date = date
		if time:
			self.time = time
