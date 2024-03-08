class Budget:
	def __init__(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.usage = {category: 0 for category in breakdown}

	def set_budget(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.usage = {category: 0 for category in breakdown}

	def update_budget(self, category, amount):
		if category not in self.breakdown:
			print(f'Category {category} does not exist in the budget breakdown.')
			return
		self.breakdown[category] += amount
		self.total_budget += amount

	def track_usage(self, category, amount):
		if category not in self.usage:
			print(f'Category {category} does not exist in the budget breakdown.')
			return
		self.usage[category] += amount
		if self.usage[category] > self.breakdown[category]:
			print(f'Alert: Budget for {category} exceeded.')
		if sum(self.usage.values()) > self.total_budget:
			print('Alert: Total budget exceeded.')
