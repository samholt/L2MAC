from dataclasses import dataclass
from cryptography.fernet import Fernet

@dataclass
class Message:
	id: str
	sender_id: str
	receiver_id: str
	content: str
	status: str = 'sent'
	key: str = Fernet.generate_key().decode()

	def set_status(self, status):
		self.status = status

	def get_status(self):
		return self.status

	def encrypt_content(self):
		cipher_suite = Fernet(self.key)
		self.content = cipher_suite.encrypt(self.content.encode()).decode()

	def decrypt_content(self):
		cipher_suite = Fernet(self.key)
		self.content = cipher_suite.decrypt(self.content.encode()).decode()

