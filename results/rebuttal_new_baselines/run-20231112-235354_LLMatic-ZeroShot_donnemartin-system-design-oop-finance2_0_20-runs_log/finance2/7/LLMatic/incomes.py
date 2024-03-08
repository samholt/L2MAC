class Income:
	def __init__(self, id, amount, source, date):
		self.id = id
		self.amount = amount
		self.source = source
		self.date = date

	def update(self, amount=None, source=None, date=None):
		if amount is not None:
			self.amount = amount
		if source is not None:
			self.source = source
		if date is not None:
			self.date = date

	def delete(self):
		del self
