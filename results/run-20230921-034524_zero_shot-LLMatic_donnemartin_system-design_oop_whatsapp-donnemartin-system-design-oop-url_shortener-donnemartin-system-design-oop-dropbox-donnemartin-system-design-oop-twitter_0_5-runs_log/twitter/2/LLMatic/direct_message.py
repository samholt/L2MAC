class DirectMessage:
	def __init__(self, sender, receiver, message):
		self.sender = sender
		self.receiver = receiver
		self.message = message

	def send_message(self):
		self.receiver.inbox.append(self)
		self.receiver.direct_messages.append(self)

	def receive_message(self):
		return self.receiver.inbox
