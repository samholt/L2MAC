from cryptography.fernet import Fernet

# Mock database
activity_log = {}


class Security:

	def __init__(self, key=None):
		self.key = key or Fernet.generate_key()
		self.cipher_suite = Fernet(self.key)

	def encrypt(self, data):
		return self.cipher_suite.encrypt(data)

	def decrypt(self, data):
		return self.cipher_suite.decrypt(data)

	@staticmethod
	def log_activity(user_id, action):
		if user_id not in activity_log:
			activity_log[user_id] = []
		activity_log[user_id].append(action)

	@staticmethod
	def get_activity(user_id):
		return activity_log.get(user_id, [])
