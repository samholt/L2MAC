class Notification:
	def __init__(self):
		self.notifications = {}

	def add_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

	def clear_notifications(self, user_id):
		self.notifications[user_id] = []

	def send_notification(self, user_id, message):
		# This is a mock function. In a real system, this would send an email or SMS.
		print(f'Sending notification to {user_id}: {message}')
		self.add_notification(user_id, message)
