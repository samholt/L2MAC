class Notification:
	def __init__(self):
		self.notifications = {}

	def set_notification(self, user_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(notification)
		return 'Notification set successfully'

	def get_notifications(self, user_id):
		if user_id in self.notifications:
			return self.notifications[user_id]
		return 'No notifications found'

	def alert_unusual_activity(self, user_id, alert):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(alert)
		return 'Alert set successfully'
