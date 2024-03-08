from user import User

class Chat:
	def __init__(self, user1: User, user2: User):
		self.user1 = user1
		self.user2 = user2
		self.messages = []
		self.read_receipts = {}

	def send_message(self, sender: User, receiver: User, message: str):
		self.messages.append((sender, receiver, message))
		self.read_receipts[(sender, receiver, message)] = False

	def receive_message(self, sender: User, receiver: User, message: str):
		if (sender, receiver, message) in self.messages:
			self.read_receipts[(sender, receiver, message)] = True

	def display_read_receipts(self):
		return self.read_receipts

	def encrypt_message(self, message: str):
		# Placeholder for encryption logic
		return message

	def decrypt_message(self, message: str):
		# Placeholder for decryption logic
		return message
