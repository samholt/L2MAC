class Message:
	def __init__(self, sender, receiver, text):
		self.sender = sender
		self.receiver = receiver
		self.text = text
		self.is_blocked = False

	def send(self):
		if not self.is_blocked:
			self.receiver.inbox.append(self)
			return True
		return False

	def block(self):
		self.is_blocked = True

	def unblock(self):
		self.is_blocked = False
