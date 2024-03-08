class DirectMessage:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content

	def get_sender(self):
		return self.sender

	def get_receiver(self):
		return self.receiver

	def get_content(self):
		return self.content
