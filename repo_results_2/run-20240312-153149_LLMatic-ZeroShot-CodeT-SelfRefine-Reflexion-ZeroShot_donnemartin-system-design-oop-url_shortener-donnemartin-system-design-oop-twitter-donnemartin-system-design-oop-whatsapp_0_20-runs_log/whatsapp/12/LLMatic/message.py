class Message:
	def __init__(self, sender, recipient, content, read_status=False, encryption_status=False):
		self.sender = sender
		self.recipient = recipient
		self.content = content
		self.read_status = read_status
		self.encryption_status = encryption_status

	def encrypt(self):
		self.content = ''.join(chr(ord(c) + 3) for c in self.content)
		self.encryption_status = True

	def decrypt(self):
		if self.encryption_status:
			self.content = ''.join(chr(ord(c) - 3) for c in self.content)
			self.encryption_status = False

	def read(self):
		self.read_status = True
