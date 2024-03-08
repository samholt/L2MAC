class Budget:
	def __init__(self, monthly_budget):
		self.monthly_budget = monthly_budget
		self.alerts = []

	def set_budget(self, new_budget):
		self.monthly_budget = new_budget

	def adjust_budget(self, adjustment):
		self.monthly_budget += adjustment

	def generate_alert(self, current_spending):
		if current_spending >= self.monthly_budget * 0.9:
			self.alerts.append('You are nearing your budget limit.')

	def get_alerts(self):
		return self.alerts
