class Account:
	def __init__(self):
		self.balance = 0
		self.transactions = []
		self.linked_banks = []

	def link_bank(self, bank):
		self.linked_banks.append(bank)

	def import_transactions(self, bank):
		if bank in self.linked_banks:
			self.transactions.extend(bank.get_transactions())
			self.update_balance()

	def update_balance(self):
		self.balance = sum(transaction.amount for transaction in self.transactions)
