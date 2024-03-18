import datetime

class Notification:
	def __init__(self, user, notification_type):
		self.user = user
		self.notification_type = notification_type
		self.created_at = datetime.datetime.now()

	def create_notification(self):
		self.user.notifications.append(self)

	def view_notifications(self):
		return [{'notification_type': notification.notification_type, 'created_at': notification.created_at} for notification in self.user.notifications]
