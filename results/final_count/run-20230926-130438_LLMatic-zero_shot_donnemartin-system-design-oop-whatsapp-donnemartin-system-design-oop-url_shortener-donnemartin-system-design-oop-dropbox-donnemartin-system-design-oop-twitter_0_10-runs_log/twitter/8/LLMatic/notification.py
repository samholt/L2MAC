class Notification:
	def __init__(self, user, event):
		self.user = user
		self.event = event

	def send_notification(self):
		return f'Notification for {self.user}: {self.event}'
