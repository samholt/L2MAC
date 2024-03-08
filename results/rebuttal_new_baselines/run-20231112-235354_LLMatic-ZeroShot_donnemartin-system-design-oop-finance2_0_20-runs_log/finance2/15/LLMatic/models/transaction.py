from datetime import datetime


class Transaction:
	def __init__(self, user, amount, category, type, date=None):
		self.user = user
		self.amount = amount
		self.category = category
		self.type = type
		self.date = date if date else datetime.now()

	@classmethod
	def create(cls, user, amount, category, type, date=None):
		transaction = cls(user, amount, category, type, date)
		# Here we should add the transaction to the database
		# But as we don't have a database, we will use a dictionary to simulate it
		DATABASE.setdefault(user, []).append(transaction)
		return transaction

	@staticmethod
	def get_transactions(user):
		# Here we should retrieve the transactions from the database
		# But as we don't have a database, we will use a dictionary to simulate it
		return DATABASE.get(user, [])


# Mock database
DATABASE = {}
