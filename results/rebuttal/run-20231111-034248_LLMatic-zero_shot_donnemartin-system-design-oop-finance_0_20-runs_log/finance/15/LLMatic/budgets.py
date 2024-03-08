class Budget:
	def __init__(self):
		self.budgets = {}

	def set_budget(self, category, amount):
		self.budgets[category] = amount

	def get_budget(self, category):
		return self.budgets.get(category, 0)

	def check_budget(self, category, amount):
		budget = self.get_budget(category)
		if amount > budget:
			return 'Exceeded'
		elif amount >= budget * 0.9:
			return 'Nearing'
		else:
			return 'Safe'

	def track_progress(self, category, amount):
		budget = self.get_budget(category)
		return (amount / budget) * 100 if budget else 0
