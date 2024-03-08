import hashlib


class User:
	def __init__(self, username, password):
		self.username = username
		self.password = self.encrypt_password(password)
		self.transactions = []
		self.balance = 0

	def encrypt_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def check_password(self, password):
		return self.password == self.encrypt_password(password)

	def change_password(self, new_password):
		self.password = self.encrypt_password(new_password)
		return True

	def recover_password(self):
		# In a real system, this should send an email or SMS with a recovery link
		return 'Recovery link has been sent to your email.'
