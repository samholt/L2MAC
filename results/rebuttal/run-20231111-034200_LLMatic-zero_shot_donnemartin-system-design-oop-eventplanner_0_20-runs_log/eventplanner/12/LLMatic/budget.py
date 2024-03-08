class Budget:
	def __init__(self):
		self.total_budget = 0
		self.category_budget = {}
		self.expenses = {}

	def set_budget(self, total_budget, category_budget):
		self.total_budget = total_budget
		self.category_budget = category_budget

	def track_expense(self, category, amount):
		if category not in self.expenses:
			self.expenses[category] = 0
		self.expenses[category] += amount

	def check_budget(self):
		total_expense = sum(self.expenses.values())
		if total_expense > self.total_budget:
			return 'Budget Overrun'
		else:
			return 'Within Budget'
