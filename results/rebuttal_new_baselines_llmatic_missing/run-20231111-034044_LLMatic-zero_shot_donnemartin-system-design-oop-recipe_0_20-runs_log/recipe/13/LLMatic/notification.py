class Notification:
	def __init__(self, user):
		self.user = user

	def notify(self, message):
		# Mock implementation of user notification
		# In a real-world scenario, this would involve sending an email or push notification
		return f'Notification for {self.user}: {message}'
