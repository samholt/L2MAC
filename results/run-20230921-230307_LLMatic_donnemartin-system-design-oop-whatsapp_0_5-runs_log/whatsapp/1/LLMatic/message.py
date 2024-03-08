class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content

	def get_content(self):
		return self.content

	def set_content(self, content):
		self.content = content
