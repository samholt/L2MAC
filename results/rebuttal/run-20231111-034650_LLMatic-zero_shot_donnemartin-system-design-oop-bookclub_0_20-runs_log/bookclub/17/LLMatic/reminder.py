class Reminder:
	def __init__(self):
		self.id = None
		self.meeting_id = None
		self.time = None
		self.message = None

	def create_reminder(self, meeting_id, time, message):
		# Mock database interaction
		reminders_db = {}
		reminder_id = len(reminders_db) + 1
		reminders_db[reminder_id] = {'meeting_id': meeting_id, 'time': time, 'message': message}
		return reminder_id

	def get_reminder(self, id):
		# Mock database interaction
		reminders_db = {}
		return reminders_db.get(id, 'Reminder not found')

	def update_reminder(self, id, meeting_id, time, message):
		# Mock database interaction
		reminders_db = {}
		if id in reminders_db:
			reminders_db[id] = {'meeting_id': meeting_id, 'time': time, 'message': message}
			return 'Reminder updated'
		return 'Reminder not found'

	def delete_reminder(self, id):
		# Mock database interaction
		reminders_db = {}
		if id in reminders_db:
			del reminders_db[id]
			return 'Reminder deleted'
		return 'Reminder not found'
