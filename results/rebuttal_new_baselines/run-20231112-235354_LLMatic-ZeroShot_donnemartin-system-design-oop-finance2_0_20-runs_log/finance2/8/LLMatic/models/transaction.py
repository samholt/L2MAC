from datetime import datetime


class Transaction:
	def __init__(self, user, amount, category):
		self.user = user
		self.amount = amount
		self.category = category
		self.date = datetime.now()

	@classmethod
	def create_transaction(cls, user, amount, category):
		return cls(user, amount, category)

	@staticmethod
	def get_user_transactions(user, transactions):
		# This is a mock function, in a real application this would interact with a database
		return [transaction for transaction in transactions if transaction.user == user]

	@staticmethod
	def categorize_transactions(transactions, category):
		# This is a mock function, in a real application this would interact with a database
		return [transaction for transaction in transactions if transaction.category == category]
