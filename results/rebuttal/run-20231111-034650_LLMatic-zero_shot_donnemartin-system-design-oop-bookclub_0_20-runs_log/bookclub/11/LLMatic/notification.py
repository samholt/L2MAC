class Notification:
	def __init__(self):
		self.notifications = {}

	def send_notification(self, user, message):
		if user not in self.notifications:
			self.notifications[user] = []
		self.notifications[user].append(message)
		return 'Notification sent to {}'.format(user)

	def send_email_alert(self, user, message):
		# In a real system, here we would use an email service to send the email.
		# For this task, we will just simulate this with a print statement.
		print('Email sent to {}: {}'.format(user, message))
		return 'Email alert sent to {}'.format(user)
