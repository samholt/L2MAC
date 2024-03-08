class Notification:
	def __init__(self, type, recipient, content):
		self.type = type
		self.recipient = recipient
		self.content = content

	def send_notification(self):
		return f'Sending {self.type} notification to {self.recipient} with content: {self.content}'

	def set_reminder(self, time):
		return f'Setting reminder for {self.recipient} at {time} with content: {self.content}'
