class Notification:
	def __init__(self):
		self.notifications = {}

	def add_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

	def send_email_alert(self, user_id, message):
		# Mock email sending functionality
		print(f'Sending email to {user_id} with message: {message}')
