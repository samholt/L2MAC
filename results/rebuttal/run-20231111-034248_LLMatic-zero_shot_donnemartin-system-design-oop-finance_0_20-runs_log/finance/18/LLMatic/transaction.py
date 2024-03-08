from datetime import datetime


class Transaction:
	def __init__(self, amount, category, description='', date=None):
		self.amount = amount
		self.category = category
		self.description = description
		self.date = date if date else datetime.now()

	def create_transaction(self, amount, category, description='', date=None):
		return Transaction(amount, category, description, date)

	def categorize_transaction(self, category):
		self.category = category

	def is_recurring(self, transactions):
		return self.category in [transaction.category for transaction in transactions]
