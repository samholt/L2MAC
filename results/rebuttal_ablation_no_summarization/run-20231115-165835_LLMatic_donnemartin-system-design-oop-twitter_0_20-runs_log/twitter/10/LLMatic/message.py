class Message:
	def __init__(self, sender, recipient, content):
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.blocked_users = []

	def send_message(self):
		if self.sender in self.recipient.blocked_users:
			return 'You have been blocked by the recipient.'
		else:
			self.recipient.messages.append(self)
			return 'Message sent successfully'

	def block_user(self, user):
		if user not in self.blocked_users:
			self.blocked_users.append(user)
			return 'User blocked successfully'
		else:
			return 'User is already blocked'

	def unblock_user(self, user):
		if user in self.blocked_users:
			self.blocked_users.remove(user)
			return 'User unblocked successfully'
		else:
			return 'User is not blocked'
