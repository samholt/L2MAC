from datetime import datetime


class Transaction:
	def __init__(self, user, amount, category, date=None):
		self.user = user
		self.amount = amount
		self.category = category
		self.date = date if date else datetime.now()

	@classmethod
	def create(cls, user, amount, category, date=None):
		return cls(user, amount, category, date)

	@staticmethod
	def get_user_transactions(user):
		# This should interact with a real database
		# For now, we'll use a mock in-memory database
		mock_db = {}
		return mock_db.get(user, [])

	def categorize(self, category):
		self.category = category
