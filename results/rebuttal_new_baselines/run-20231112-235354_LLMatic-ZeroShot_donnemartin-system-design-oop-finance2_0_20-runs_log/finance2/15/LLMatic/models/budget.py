class Budget:
	def __init__(self, user, amount, categories):
		self.user = user
		self.amount = amount
		self.categories = categories

	def set_budget(self, amount, categories):
		self.amount = amount
		self.categories = categories

	def get_budget(self):
		return {'user': self.user, 'amount': self.amount, 'categories': self.categories}
