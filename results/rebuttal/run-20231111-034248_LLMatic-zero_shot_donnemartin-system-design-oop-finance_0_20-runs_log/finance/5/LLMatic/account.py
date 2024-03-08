class Account:
	def __init__(self, account_number, bank_name):
		self.account_number = account_number
		self.bank_name = bank_name
		self.balance = 0
		self.transactions = []

	def link_account(self, account_number, bank_name):
		self.account_number = account_number
		self.bank_name = bank_name

	def import_transactions(self, transactions):
		self.transactions.extend(transactions)
		self.update_balance()

	def update_balance(self):
		self.balance = sum(transaction.amount for transaction in self.transactions)

