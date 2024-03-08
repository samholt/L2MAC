class Budget:
	def __init__(self, user, amount, category):
		self.user = user
		self.amount = amount
		self.category = category
		self.budgets = {}

	def set_budget(self, user, amount, category):
		self.budgets[user] = {'amount': amount, 'category': category}

	def adjust_budget(self, user, amount):
		if user in self.budgets:
			self.budgets[user]['amount'] += amount

	def get_budgets(self, user):
		if user in self.budgets:
			return self.budgets[user]
		return None
