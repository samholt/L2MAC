class Meeting:
	def __init__(self):
		self.meetings = {}

	def schedule_meeting(self, book_club_id, meeting_id, meeting_time):
		if book_club_id not in self.meetings:
			self.meetings[book_club_id] = {}
		self.meetings[book_club_id][meeting_id] = {'time': meeting_time, 'reminder_set': False}

	def set_reminder(self, book_club_id, meeting_id):
		if book_club_id in self.meetings and meeting_id in self.meetings[book_club_id]:
			self.meetings[book_club_id][meeting_id]['reminder_set'] = True
