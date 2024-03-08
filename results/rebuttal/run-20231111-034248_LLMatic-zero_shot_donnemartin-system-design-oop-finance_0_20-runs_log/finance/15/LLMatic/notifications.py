class Notifications:
	def __init__(self):
		self.notifications = {}

	def set_notification(self, user_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(notification)

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

	def alert_unusual_activity(self, user_id, activity):
		self.set_notification(user_id, f'Unusual activity detected: {activity}')

	def alert_upcoming_payment(self, user_id, payment):
		self.set_notification(user_id, f'Upcoming payment due: {payment}')
