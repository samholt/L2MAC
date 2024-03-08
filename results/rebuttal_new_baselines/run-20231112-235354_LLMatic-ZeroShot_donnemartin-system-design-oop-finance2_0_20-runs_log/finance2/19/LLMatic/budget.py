class Budget:
	def __init__(self):
		self.budget = 0
		self.expenses = []

	def set_budget(self, amount):
		self.budget = amount

	def adjust_budget(self, amount):
		self.budget += amount

	def add_expense(self, expense):
		self.expenses.append(expense)

	def check_budget(self):
		total_expense = sum(self.expenses)
		if total_expense >= self.budget * 0.9:
			return 'Warning: You are nearing your budget limit.'
		else:
			return 'You are within your budget limit.'

	def analyze_expenses(self):
		average_expense = sum(self.expenses) / len(self.expenses) if self.expenses else 0
		if average_expense > self.budget * 0.75:
			return 'Consider adjusting your budget.'
		elif average_expense > self.budget * 0.5:
			return 'Your budget is nearing its limit.'
		else:
			return 'Your budget is well balanced.'
