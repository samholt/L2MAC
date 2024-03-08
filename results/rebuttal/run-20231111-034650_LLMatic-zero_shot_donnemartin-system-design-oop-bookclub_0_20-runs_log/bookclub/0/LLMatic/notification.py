class Notification:
	def __init__(self, recipient, content):
		self.recipient = recipient
		self.content = content
		self.status = 'unread'

	def create_notification(self, recipient, content):
		self.recipient = recipient
		self.content = content
		self.status = 'unread'
		return self

	def update_status(self, status):
		self.status = status
		return self

	def send_email_alert(self):
		# This is a placeholder for sending email. In a real system, we would integrate with an email service here.
		print(f'Sending email to {self.recipient} with content: {self.content}')
		return self
