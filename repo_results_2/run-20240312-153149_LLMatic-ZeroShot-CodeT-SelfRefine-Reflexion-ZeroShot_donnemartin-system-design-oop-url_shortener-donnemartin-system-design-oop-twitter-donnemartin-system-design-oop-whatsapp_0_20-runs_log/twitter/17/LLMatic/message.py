import datetime


class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = datetime.datetime.now()
		self.blocked_users = []

	def send(self):
		if self.sender in self.blocked_users:
			return 'User is blocked'
		else:
			return 'Message sent'

	def block(self, user):
		self.blocked_users.append(user)
		return 'User blocked'
