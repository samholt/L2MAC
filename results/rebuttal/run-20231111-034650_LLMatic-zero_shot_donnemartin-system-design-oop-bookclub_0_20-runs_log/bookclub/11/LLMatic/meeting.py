class Meeting:
	def __init__(self):
		self.meetings = {}

	def schedule_meeting(self, date_time, book_club, attendees):
		if book_club not in self.meetings:
			self.meetings[book_club] = []
		self.meetings[book_club].append({'date_time': date_time, 'attendees': attendees})
		return 'Meeting scheduled successfully'

	def send_reminders(self, book_club):
		if book_club not in self.meetings:
			return 'No meetings scheduled for this book club'
		return 'Reminders sent for all meetings of this book club'
