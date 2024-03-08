class DirectMessage:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content

	def send_message(self):
		self.receiver.direct_messages.append(self)

	def receive_message(self):
		# This method will be implemented in the User class
		pass
