import datetime

# Mock database
notifications_db = {}


class Notification:
	def __init__(self, user_id, type, message):
		self.user_id = user_id
		self.type = type
		self.message = message
		self.time = datetime.datetime.now()

	def send_notification(self):
		# In a real system, this would send an email or SMS
		# Here we just add the notification to the mock database
		notifications_db[self.user_id] = {'type': self.type, 'message': self.message, 'time': self.time}

	def set_reminder(self, reminder_time):
		# In a real system, this would set a reminder
		# Here we just add the reminder to the mock database
		notifications_db[self.user_id] = {'type': 'reminder', 'message': self.message, 'time': reminder_time}
