class Budget:
	def __init__(self, total_budget, breakdown, alerts):
		self.total_budget = total_budget
		self.breakdown = breakdown
		self.alerts = alerts

	def set_budget(self, total_budget):
		self.total_budget = total_budget

	def track_budget(self):
		return self.total_budget

	def alert_overrun(self):
		if self.total_budget < 0:
			return 'Budget Overrun'
		else:
			return 'Budget is under control'

budgets = {}

