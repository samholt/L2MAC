class Budget:
	def __init__(self, total_budget):
		self.total_budget = total_budget
		self.category_budgets = {}
		self.category_spent = {}

	def set_category_budget(self, category, budget):
		self.category_budgets[category] = budget

	def track_spending(self, category, amount):
		if category not in self.category_spent:
			self.category_spent[category] = 0
		self.category_spent[category] += amount

	def alert_overrun(self):
		for category, budget in self.category_budgets.items():
			spent = self.category_spent.get(category, 0)
			if spent > budget:
				return f'Alert: Budget overrun in {category}!'
		return 'No budget overruns.'
