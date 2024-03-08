class Budget:
	def __init__(self):
		self.budget = {}

	def set_budget(self, category, amount):
		self.budget[category] = amount

	def adjust_budget(self, category, amount):
		if category in self.budget:
			self.budget[category] += amount

	def get_budget(self, category):
		return self.budget.get(category, 0)

	def alert(self):
		alerts = []
		for category, amount in self.budget.items():
			if amount < 100:
				alerts.append(f'Low budget alert for {category}!')
		return alerts

	def analyze_spending(self, expenses):
		for category, amount in expenses.items():
			if category in self.budget and self.budget[category] < amount:
				self.budget[category] = amount + 100
				print(f'Budget for {category} has been increased to {self.budget[category]}')
		return self.budget
