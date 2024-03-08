class Notifications:
	def __init__(self):
		self.notifications_db = {}

	def send_notification(self, user_id, message):
		if user_id not in self.notifications_db:
			self.notifications_db[user_id] = []
		self.notifications_db[user_id].append(message)
		return 'Notification sent'

	def alert_user(self, user_id, alert_message):
		if user_id not in self.notifications_db:
			self.notifications_db[user_id] = []
		self.notifications_db[user_id].append(alert_message)
		return 'Alert sent'

	def get_notifications(self, user_id):
		if user_id in self.notifications_db:
			return self.notifications_db[user_id]
		return []
