class BankAccount:
	def __init__(self):
		self.accounts = {}

	def link_account(self, account_id, initial_balance):
		self.accounts[account_id] = {'balance': initial_balance, 'transactions': []}

	def import_transactions(self, account_id, transactions):
		self.accounts[account_id]['transactions'].extend(transactions)
		self.update_balance(account_id)

	def update_balance(self, account_id):
		self.accounts[account_id]['balance'] = self.accounts[account_id]['balance'] + sum([transaction['amount'] for transaction in self.accounts[account_id]['transactions']])
		self.accounts[account_id]['transactions'] = []

	def get_account(self, account_id):
		return self.accounts.get(account_id, None)
