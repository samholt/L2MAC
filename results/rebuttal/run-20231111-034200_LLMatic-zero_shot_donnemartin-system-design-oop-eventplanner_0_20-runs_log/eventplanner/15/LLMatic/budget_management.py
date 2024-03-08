class Budget:
	def __init__(self):
		self.budget = 0
		self.expenses = 0

	def set_budget(self, amount):
		self.budget = amount

	def track_expense(self, amount):
		self.expenses += amount
		if self.expenses > self.budget:
			self.alert_overrun()

	def alert_overrun(self):
		print('Budget overrun!')

