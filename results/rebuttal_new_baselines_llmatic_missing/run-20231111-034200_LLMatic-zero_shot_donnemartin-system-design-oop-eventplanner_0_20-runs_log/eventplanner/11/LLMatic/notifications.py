class Notifications:
	def __init__(self):
		self.notifications = {}

	def add_notification(self, user_id, event_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = {}
		self.notifications[user_id][event_id] = notification

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, {})

	def remove_notification(self, user_id, event_id):
		if user_id in self.notifications and event_id in self.notifications[user_id]:
			del self.notifications[user_id][event_id]
