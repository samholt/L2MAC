class Notifications:
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

	def set_reminder(self, user_id, event_id, reminder_time):
		self.notifications[user_id].append({'event_id': event_id, 'reminder_time': reminder_time})

	def get_reminders(self, user_id):
		return [notification for notification in self.notifications.get(user_id, []) if 'reminder_time' in notification]
