class Budget:
	def __init__(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.alerts = []

	def set_budget(self, total_budget, breakdown):
		self.total_budget = total_budget
		self.breakdown = breakdown

	def track_budget(self, category, amount):
		if category in self.breakdown:
			self.breakdown[category] -= amount
			if self.breakdown[category] < 0:
				self.alerts.append(f'Over budget in {category} by {-self.breakdown[category]}')
		return self.breakdown

	def get_alerts(self):
		return self.alerts

mock_database = {}

