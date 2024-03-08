class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bank_accounts = []
		self.mfa_enabled = False

	def create_account(self, username, password):
		self.username = username
		self.password = password

	def link_bank_account(self, account_number):
		self.bank_accounts.append(account_number)

	def enable_mfa(self):
		self.mfa_enabled = True

	def disable_mfa(self):
		self.mfa_enabled = False
