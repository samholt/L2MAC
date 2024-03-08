class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bank_accounts = []

	def create_user(self, username, password):
		self.username = username
		self.password = password

	def update_user(self, username, password):
		self.username = username
		self.password = password

	def delete_user(self):
		self.username = None
		self.password = None
		self.bank_accounts = []

	def link_bank_account(self, account_number):
		self.bank_accounts.append(account_number)
