from cryptography.fernet import Fernet


class Message:
	def __init__(self, sender, receiver, content, read_status=False):
		self.sender = sender
		self.receiver = receiver
		self.content = content
		self.read_status = read_status

	def send_message(self):
		return self

	def receive_message(self, message):
		self.content = message.content
		self.sender = message.sender
		self.receiver = message.receiver
		self.read_status = False

	def read_receipt(self):
		self.read_status = True

	def encrypt_message(self, key):
		cipher_suite = Fernet(key)
		self.content = cipher_suite.encrypt(self.content.encode()).decode()

	def decrypt_message(self, key):
		cipher_suite = Fernet(key)
		self.content = cipher_suite.decrypt(self.content.encode()).decode()
