import hashlib

class User:
	def __init__(self, username, password, email):
		self.username = username
		self.password = self.hash_password(password)
		self.email = email
		self.bank_accounts = []

	def hash_password(self, password):
		return hashlib.sha256(password.encode()).hexdigest()

	def authenticate(self, password):
		return self.password == self.hash_password(password)

	def link_bank_account(self, bank_account):
		self.bank_accounts.append(bank_account)

