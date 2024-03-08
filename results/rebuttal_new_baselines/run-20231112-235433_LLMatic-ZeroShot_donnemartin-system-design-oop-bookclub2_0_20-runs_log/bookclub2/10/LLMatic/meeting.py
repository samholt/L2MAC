from datetime import datetime


class Meeting:
	def __init__(self, id, date_time, book_club):
		self.id = id
		self.date_time = date_time
		self.book_club = book_club

	def schedule_new_meeting(self, date_time):
		self.date_time = date_time

	def send_reminders(self):
		for member in self.book_club.members:
			print(f'Reminder sent to {member.name} for meeting on {self.date_time}')
