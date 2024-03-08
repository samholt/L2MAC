class Notifications:
	def __init__(self):
		self.notifications_db = {}

	def send_notification(self, user_id, message):
		if user_id not in self.notifications_db:
			self.notifications_db[user_id] = []
		self.notifications_db[user_id].append(message)
		return 'Notification sent'

	def set_reminder(self, user_id, reminder):
		if user_id not in self.notifications_db:
			self.notifications_db[user_id] = []
		self.notifications_db[user_id].append(reminder)
		return 'Reminder set'
