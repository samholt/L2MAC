import datetime


class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text
		self.timestamp = datetime.datetime.now()
		self.id = id(self)
		self.blocked_users = []

	def send(self, db):
		if self.receiver in self.blocked_users:
			return 'User is blocked'
		else:
			db[self.id] = self
			return 'Message sent'

	def block_user(self, user):
		self.blocked_users.append(user)
		return 'User blocked'

	def unblock_user(self, user):
		self.blocked_users.remove(user)
		return 'User unblocked'
