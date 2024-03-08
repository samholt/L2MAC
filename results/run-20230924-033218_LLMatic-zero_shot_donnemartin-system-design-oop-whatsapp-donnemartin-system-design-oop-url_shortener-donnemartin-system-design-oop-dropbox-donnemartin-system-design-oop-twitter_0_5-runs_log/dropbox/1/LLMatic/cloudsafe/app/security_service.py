from cryptography.fernet import Fernet
from cloudsafe.app.models import ActivityLog


class SecurityService:
	def __init__(self, secret_key):
		self.cipher_suite = Fernet(secret_key)

	def encrypt_file(self, file):
		# Encrypt the file
		encrypted_file = self.cipher_suite.encrypt(file)
		return encrypted_file

	def decrypt_file(self, encrypted_file):
		# Decrypt the file
		decrypted_file = self.cipher_suite.decrypt(encrypted_file)
		return decrypted_file

	def log_activity(self, user_id, action):
		# Log the user's activity
		activity_log = ActivityLog(user_id=user_id, action=action)
		activity_log.save()
		return activity_log
