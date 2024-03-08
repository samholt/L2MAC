class Notification:
	def __init__(self, user, content):
		self.user = user
		self.content = content

	# Mock database
	notifications = {}

	def create_notification(self):
		Notification.notifications[self.user] = {'content': self.content}
		return Notification.notifications

