class Notification:
	def __init__(self, type, message):
		self.type = type
		self.message = message

	def send_notification(self):
		print(f'Sending {self.type} notification: {self.message}')


class Reminder:
	def __init__(self, message, time):
		self.message = message
		self.time = time

	def set_reminder(self):
		print(f'Setting reminder for {self.time}: {self.message}')
