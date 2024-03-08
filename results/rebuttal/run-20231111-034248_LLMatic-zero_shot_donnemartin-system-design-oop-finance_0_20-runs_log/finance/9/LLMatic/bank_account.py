class BankAccount:
	def __init__(self, account_number, balance=0):
		self.account_number = account_number
		self.balance = balance
		self.transactions = []

	def link_account(self, account_number):
		self.account_number = account_number

	def import_transactions(self, transactions):
		self.transactions.extend(transactions)
		self.update_balance()

	def update_balance(self):
		self.balance = sum(transaction.amount for transaction in self.transactions if transaction.type == 'debit') - sum(transaction.amount for transaction in self.transactions if transaction.type == 'credit')


class BankAccountManager:
	def __init__(self):
		self.bank_accounts = {}

	def link_account(self, account_number):
		if account_number not in self.bank_accounts:
			self.bank_accounts[account_number] = BankAccount(account_number)

	def import_transactions(self, account_number, transactions):
		if account_number in self.bank_accounts:
			self.bank_accounts[account_number].import_transactions(transactions)

	def update_balance(self, account_number):
		if account_number in self.bank_accounts:
			self.bank_accounts[account_number].update_balance()
