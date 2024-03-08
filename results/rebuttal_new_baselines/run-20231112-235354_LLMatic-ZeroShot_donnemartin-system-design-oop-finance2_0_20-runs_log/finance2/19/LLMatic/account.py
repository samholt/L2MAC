class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bank_account_linked = False
		self.multi_factor_auth = False

	def create_user(self):
		# Simulate user creation
		return {'username': self.username, 'password': self.password}

	def link_bank_account(self):
		# Simulate linking bank account
		self.bank_account_linked = True
		return self.bank_account_linked

	def enable_multi_factor_auth(self):
		# Simulate enabling multi-factor authentication
		self.multi_factor_auth = True
		return self.multi_factor_auth
