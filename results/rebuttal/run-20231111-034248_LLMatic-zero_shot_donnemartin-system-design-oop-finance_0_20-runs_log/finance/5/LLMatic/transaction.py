class Transaction:
	def __init__(self, amount, category, date, is_recurring, is_deposit):
		self.amount = amount
		self.category = category
		self.date = date
		self.is_recurring = is_recurring
		self.is_deposit = is_deposit

	def enter_transaction(self, amount, category, date, is_deposit):
		self.amount = amount
		self.category = category
		self.date = date
		self.is_deposit = is_deposit

	def categorize_transaction(self, category):
		self.category = category

	def check_recurring(self, transactions):
		for transaction in transactions:
			if transaction.date == self.date and transaction.amount == self.amount and transaction.category == self.category:
				self.is_recurring = True
				break
