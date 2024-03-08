class User:
	def __init__(self, username, email, password, role='member'):
		self.username = username
		self.email = email
		self.password = password
		self.role = role

class BookClub:
	def __init__(self, name, privacy_setting, creator):
		self.name = name
		self.privacy_setting = privacy_setting
		self.creator = creator
		self.members = []
		self.meetings = []

	def add_member(self, user):
		self.members.append(user)

	def update_member_role(self, user, role):
		if user in self.members:
			user.role = role

	def add_meeting(self, meeting):
		self.meetings.append(meeting)

	def update_meeting(self, meeting, date, time, location):
		if meeting in self.meetings:
			meeting.date = date
			meeting.time = time
			meeting.location = location

	def delete_meeting(self, meeting):
		if meeting in self.meetings:
			self.meetings.remove(meeting)

class Meeting:
	def __init__(self, date, time, location):
		self.date = date
		self.time = time
		self.location = location
		self.reminder_sent = False

	def is_reminder_sent(self):
		return self.reminder_sent

	def send_reminder(self):
		self.reminder_sent = True
