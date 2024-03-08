class Budget:
	def __init__(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.alerts = []

	def set_budget(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown

	def get_budget(self):
		return self.total_budget, self.breakdown

	def update_budget(self, category, amount):
		if category in self.breakdown:
			self.breakdown[category] += amount
			if self.breakdown[category] > self.total_budget:
				self.alerts.append(f'Over budget in {category}!')
		else:
			self.alerts.append(f'Category {category} does not exist.')

	def get_alerts(self):
		return self.alerts

budgets = {}

