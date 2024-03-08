class Notification:
	def __init__(self, user, content):
		self.user = user
		self.content = content

	def create_notification(self):
		return {'user': self.user, 'content': self.content}

	def send_notification(self):
		print(f'Notification sent to {self.user}: {self.content}')
