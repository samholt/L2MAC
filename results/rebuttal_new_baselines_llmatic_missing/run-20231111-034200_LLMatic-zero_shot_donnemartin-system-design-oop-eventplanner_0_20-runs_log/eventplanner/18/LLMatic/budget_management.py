class Budget:
	def __init__(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.spent = {category: 0 for category in breakdown}

	def set_budget(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.spent = {category: 0 for category in breakdown}

	def track_spending(self, category, amount):
		if category not in self.breakdown:
			return 'Invalid category'
		self.spent[category] += amount
		if self.spent[category] > self.breakdown[category]:
			return 'Budget overrun in ' + category
		return 'Spending tracked'

	def get_spent(self):
		return self.spent

	def get_remaining(self):
		remaining = {category: self.breakdown[category] - self.spent[category] for category in self.breakdown}
		return remaining
