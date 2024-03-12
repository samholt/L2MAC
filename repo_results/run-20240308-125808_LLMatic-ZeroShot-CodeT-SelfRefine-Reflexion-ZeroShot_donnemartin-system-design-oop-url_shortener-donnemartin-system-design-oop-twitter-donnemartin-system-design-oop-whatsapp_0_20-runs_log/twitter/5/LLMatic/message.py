from notification import Notification

class Message:
	def __init__(self, sender, recipient, text):
		self.sender = sender
		self.recipient = recipient
		self.text = text
		self.blocked_users = []

	def send_message(self):
		if self.sender in self.recipient.blocked_users:
			return 'You are blocked from sending messages to this user.'
		else:
			self.recipient.inbox.append(self)
			self.recipient.notifications.append(Notification(self.recipient, 'message'))
			return 'Message sent.'

	def block_user(self, user):
		self.blocked_users.append(user)
		return 'User blocked.'
