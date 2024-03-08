from datetime import datetime


class Transaction:
	def __init__(self, user, amount, type, category, date=None):
		self.user = user
		self.amount = amount
		self.type = type
		self.category = category
		self.date = date if date else datetime.now()

	def to_dict(self):
		return {
			'user': self.user,
			'amount': self.amount,
			'type': self.type,
			'category': self.category,
			'date': self.date
		}

	@staticmethod
	def create(user, amount, type, category):
		return Transaction(user, amount, type, category)

	@staticmethod
	def get_transactions(user):
		# This should be replaced with a real database call
		return []

	@staticmethod
	def categorize(transaction, category):
		transaction.category = category
		return transaction
