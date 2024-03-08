class Budget:
	def __init__(self, user, amount, category):
		self.user = user
		self.amount = amount
		self.category = category
		self.limit_nearing = False

	def set_budget(self, amount):
		self.amount = amount

	def adjust_budget(self, amount):
		self.amount += amount

	def check_budget_limit(self):
		if self.amount <= 100:
			self.limit_nearing = True
		return self.limit_nearing
