class Message:
	def __init__(self, sender, receiver, content, read_receipt, encryption, image):
		self.id = id(self)
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = read_receipt
		self.encryption = encryption
		self.image = image
