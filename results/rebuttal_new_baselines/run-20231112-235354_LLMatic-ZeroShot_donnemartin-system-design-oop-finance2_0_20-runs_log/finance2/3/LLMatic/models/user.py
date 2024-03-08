import hashlib

class User:
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = hashlib.sha256(password.encode()).hexdigest()
		self.bank_accounts = []

	@staticmethod
	def create_user(name, email, password):
		new_user = User(name, email, password)
		return new_user

	@staticmethod
	def authenticate_user(email, password):
		# Mocking user authentication
		if password == 'password':
			return True
		return False

	def link_bank_account(self, bank_account):
		# Mocking linking bank account
		self.bank_accounts.append(bank_account)
		return self.bank_accounts
