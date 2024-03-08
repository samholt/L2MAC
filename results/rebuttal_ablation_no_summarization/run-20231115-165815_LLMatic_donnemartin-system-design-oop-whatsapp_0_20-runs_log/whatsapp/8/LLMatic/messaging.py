class Messaging:
	def __init__(self):
		self.messages = {}
		self.read_receipts = {}
		self.encryption_key = 'encryption_key'

	def send_message(self, message, recipient):
		if recipient not in self.messages:
			self.messages[recipient] = []
		self.messages[recipient].append(message)

	def receive_message(self, message, sender):
		if sender not in self.messages:
			self.messages[sender] = []
		self.messages[sender].append(message)
		self.read_receipts[message] = False

	def display_read_receipt(self, message):
		if message in self.read_receipts and self.read_receipts[message] == False:
			self.read_receipts[message] = True
			return 'Message has been read'
		return 'Message has not been read'

	def encrypt_message(self, message):
		encrypted_message = ''.join(chr(ord(c) + 3) for c in message)
		return encrypted_message

	def decrypt_message(self, encrypted_message):
		decrypted_message = ''.join(chr(ord(c) - 3) for c in encrypted_message)
		return decrypted_message

	def share_image(self, image_file, recipient):
		if recipient not in self.messages:
			self.messages[recipient] = []
		self.messages[recipient].append(image_file)
