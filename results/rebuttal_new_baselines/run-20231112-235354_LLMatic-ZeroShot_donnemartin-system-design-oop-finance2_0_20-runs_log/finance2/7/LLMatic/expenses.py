class Expense:
	def __init__(self, id, amount, category, date):
		self.id = id
		self.amount = amount
		self.category = category
		self.date = date

	def update(self, amount=None, category=None, date=None):
		if amount is not None:
			self.amount = amount
		if category is not None:
			self.category = category
		if date is not None:
			self.date = date

	def delete(self):
		del self
