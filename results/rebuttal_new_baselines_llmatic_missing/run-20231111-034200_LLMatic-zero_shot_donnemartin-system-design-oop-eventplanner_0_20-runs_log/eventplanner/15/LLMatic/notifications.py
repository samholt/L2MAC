class Notification:
	def __init__(self, user, message):
		self.user = user
		self.message = message

	def send_notification(self):
		# Mock sending notification
		return f'Notification sent to {self.user}: {self.message}'

	def set_reminder(self, reminder):
		# Mock setting reminder
		return f'Reminder set for {self.user}: {reminder}'
