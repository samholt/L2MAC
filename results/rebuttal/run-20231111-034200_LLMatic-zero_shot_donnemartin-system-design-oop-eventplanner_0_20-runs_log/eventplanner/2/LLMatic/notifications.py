class Notifications:
	def __init__(self):
		self.notifications = {}

	def add_notification(self, user_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(notification)
		return True

	def get_notifications(self, user_id):
		if user_id in self.notifications:
			return self.notifications[user_id]
		return []

	def clear_notifications(self, user_id):
		if user_id in self.notifications:
			self.notifications[user_id] = []
		return True
