from cryptography.fernet import Fernet

class Message:
	def __init__(self, sender, chat, content):
		self.sender = sender
		self.chat = chat
		self.content = content
		self.status = 'sent'
		self.key = Fernet.generate_key()
		self.cipher_suite = Fernet(self.key)

	def set_status(self, status):
		self.status = status

	def get_status(self):
		return self.status

	def encrypt_content(self):
		self.content = self.cipher_suite.encrypt(self.content.encode()).decode()

	def decrypt_content(self):
		self.content = self.cipher_suite.decrypt(self.content.encode()).decode()
