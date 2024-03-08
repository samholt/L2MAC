class Budget:
	def __init__(self, total_budget):
		self.total_budget = total_budget
		self.category_budgets = {}
		self.spent = {}

	def set_category_budget(self, category, budget):
		self.category_budgets[category] = budget

	def track_spending(self, category, amount):
		if category not in self.spent:
			self.spent[category] = 0
		self.spent[category] += amount

	def alert_overrun(self):
		for category, budget in self.category_budgets.items():
			if category in self.spent and self.spent[category] > budget:
				return f'Alert: You have exceeded your budget for {category}!'
		return 'No budget overrun.'
