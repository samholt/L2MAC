class Message:
	def __init__(self, sender, recipient, text):
		self.sender = sender
		self.recipient = recipient
		self.text = text

	def send(self):
		if self.sender not in self.recipient.blocked_users:
			self.recipient.inbox.append(self)
			return True
		return False

	def receive(self):
		if self.sender not in self.recipient.blocked_users:
			self.recipient.inbox.append(self)
			return True
		return False
