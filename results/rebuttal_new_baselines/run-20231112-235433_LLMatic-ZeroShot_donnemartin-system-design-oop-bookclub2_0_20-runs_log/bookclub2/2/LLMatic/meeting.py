class Meeting:
	def __init__(self, id, date, time, attendees=[]):
		self.id = id
		self.date = date
		self.time = time
		self.attendees = attendees

	def schedule_meeting(self, id, date, time):
		self.id = id
		self.date = date
		self.time = time

	def add_attendee(self, attendee):
		self.attendees.append(attendee)

	def remove_attendee(self, attendee):
		if attendee in self.attendees:
			self.attendees.remove(attendee)

	def get_info(self):
		return {'id': self.id, 'date': self.date, 'time': self.time, 'attendees': self.attendees}
