class Notification:
	def __init__(self, id, user_id, post_id, type):
		self.id = id
		self.user_id = user_id
		self.post_id = post_id
		self.type = type

	def create_notification(self, user_id, post_id, type):
		self.id = len(Notification.notifications) + 1
		self.user_id = user_id
		self.post_id = post_id
		self.type = type
		Notification.notifications[self.id] = self

	@staticmethod
	def view_notifications(user_id):
		return [notification for notification in Notification.notifications.values() if notification.user_id == user_id]

	@staticmethod
	def clear_notifications():
		Notification.notifications.clear()

	notifications = {}
