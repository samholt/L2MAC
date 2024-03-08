class Meeting:
	def __init__(self, date, time, attendees, reminders):
		self.date = date
		self.time = time
		self.attendees = attendees
		self.reminders = reminders

	def schedule_meeting(self, date, time, attendees):
		self.date = date
		self.time = time
		self.attendees = attendees

	def update_meeting(self, date=None, time=None, attendees=None):
		if date:
			self.date = date
		if time:
			self.time = time
		if attendees:
			self.attendees = attendees

	def send_reminders(self):
		for reminder in self.reminders:
			print(f'Sending reminder: {reminder}')
