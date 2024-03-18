class Message:
	def __init__(self, sender, receiver, content):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_receipt = False
		self.encrypted = False

	def encrypt_content(self):
		self.content = ''.join(chr(ord(c) + 3) for c in self.content)
		self.encrypted = True

mock_message_db = {}
