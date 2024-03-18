import datetime


class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.timestamp = datetime.datetime.now()
		self.blocked_users = []

	def send(self):
		if self.receiver in self.blocked_users:
			return 'User is blocked'
		else:
			return 'Message sent'

	def block_user(self, user):
		self.blocked_users.append(user)
		return 'User blocked'

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
			return 'User unblocked'
		else:
			return 'User not found in blocked list'
