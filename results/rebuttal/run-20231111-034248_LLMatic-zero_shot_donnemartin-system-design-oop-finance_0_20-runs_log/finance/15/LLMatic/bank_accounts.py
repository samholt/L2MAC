class BankAccount:
	def __init__(self):
		self.accounts = {}

	def link_account(self, account_id, account_info):
		self.accounts[account_id] = account_info

	def import_transactions(self, account_id):
		# Mock implementation of importing transactions
		return 'Transactions imported'

	def get_balance(self, account_id):
		# Mock implementation of getting account balance
		return 'Account balance: 1000'

	def get_transactions(self, account_id):
		# Mock implementation of getting account transactions
		return 'Transactions: []'

