class BankAccount:
	def __init__(self, user, account_number):
		self.user = user
		self.account_number = account_number
		self.linked_accounts = []
		self.transactions = []
		self.balance = 0

	def link_account(self, account):
		self.linked_accounts.append(account)
		return 'Account linked successfully'

	def import_transactions(self, transactions):
		self.transactions.extend(transactions)
		self.update_balance()
		return 'Transactions imported successfully'

	def update_balance(self):
		self.balance = sum(transaction.amount for transaction in self.transactions)
		return 'Balance updated successfully'
