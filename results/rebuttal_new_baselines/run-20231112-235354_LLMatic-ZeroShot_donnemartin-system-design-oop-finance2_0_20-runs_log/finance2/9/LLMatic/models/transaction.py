from datetime import datetime


class Transaction:
	def __init__(self, user, amount, type, category, date=None):
		self.user = user
		self.amount = amount
		self.type = type
		self.category = category
		self.date = date if date else datetime.now()

	@classmethod
	def create(cls, user, amount, type, category, date=None):
		return cls(user, amount, type, category, date)

	@staticmethod
	def get_user_transactions(user):
		# This is a mock implementation. In a real-world application, this method would interact with a database.
		return []

	def categorize(self, category):
		self.category = category
