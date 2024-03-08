class Notification:
	def __init__(self, user, message):
		self.user = user
		self.message = message

	def send_notification(self):
		# In a real system, this would send a notification to the user
		print(f'Sending notification to {self.user}: {self.message}')

	def set_reminder(self, reminder_time):
		# In a real system, this would set a reminder for the user
		print(f'Setting reminder for {self.user} at {reminder_time}')
