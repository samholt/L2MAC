from datetime import datetime

class Meeting:
	scheduled_meetings = {}
	reminders = {}

	def schedule_meeting(self, club_id, meeting_time):
		if not club_id or not meeting_time:
			raise ValueError('Missing required parameters')
		if club_id not in self.__class__.scheduled_meetings:
			self.__class__.scheduled_meetings[club_id] = []
		self.__class__.scheduled_meetings[club_id].append(meeting_time)

	def send_reminder(self, club_id):
		if not club_id:
			raise ValueError('Missing required parameters')
		if club_id in self.__class__.scheduled_meetings:
			for meeting_time in self.__class__.scheduled_meetings[club_id]:
				if (meeting_time - datetime.now()).total_seconds() <= 86400:
					if club_id not in self.__class__.reminders:
						self.__class__.reminders[club_id] = []
					self.__class__.reminders[club_id].append(meeting_time)
					return 'Reminder sent for meeting at {}'.format(meeting_time)
			return 'No meetings within 24 hours'
		return 'No meetings scheduled for this club'
