class Notification:
	def __init__(self, type, content):
		self.type = type
		self.content = content
		self.notifications = {}

	def send_notification(self, user_id, notification):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(notification)
		return 'Notification sent'

	def set_reminder(self, user_id, reminder):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(reminder)
		return 'Reminder set'
