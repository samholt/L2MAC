class Notification:
	def __init__(self):
		self.notifications = {}

	def set_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

	def alert_unusual_activity(self, user_id, message):
		self.set_notification(user_id, f'Alert: {message}')
