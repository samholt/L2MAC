from datetime import datetime

# Mock database
transactions_db = {}

class Transaction:
	def __init__(self, user, amount, category, date=None):
		self.user = user
		self.amount = amount
		self.category = category
		self.date = date if date else datetime.now()

	@classmethod
	def create_transaction(cls, user, amount, category, date=None):
		transaction = cls(user, amount, category, date)
		transactions_db[user] = transactions_db.get(user, []) + [transaction]
		return transaction

	@classmethod
	def get_user_transactions(cls, user):
		return [transaction.__dict__ for transaction in transactions_db.get(user, [])]

	@classmethod
	def categorize_transactions(cls, user, category):
		return [transaction for transaction in transactions_db.get(user, []) if transaction.category == category]
