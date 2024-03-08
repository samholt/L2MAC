class Notifications:
	def __init__(self):
		self.notifications = {}

	def send_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)
		return 'Notification sent'

	def get_notifications(self, user_id):
		if user_id in self.notifications:
			return self.notifications[user_id]
		return 'No notifications'

	def set_reminder(self, user_id, reminder):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(reminder)
		return 'Reminder set'

	def get_reminders(self, user_id):
		if user_id in self.notifications:
			return self.notifications[user_id]
		return 'No reminders'
