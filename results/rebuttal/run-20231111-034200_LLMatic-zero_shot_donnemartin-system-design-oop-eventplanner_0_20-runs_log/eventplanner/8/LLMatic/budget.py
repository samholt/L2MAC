class Budget:
	def __init__(self):
		self.total_budget = 0
		self.category_budgets = {}
		self.category_expenses = {}

	def set_budget(self, total_budget, category_budgets):
		self.total_budget = total_budget
		self.category_budgets = category_budgets
		self.category_expenses = {category: 0 for category in category_budgets}

	def track_expense(self, category, amount):
		if category not in self.category_budgets:
			return 'Category not found'
		self.category_expenses[category] += amount
		if self.category_expenses[category] > self.category_budgets[category]:
			return 'Budget overrun in ' + category
		return 'Expense tracked'

	def get_budget_status(self):
		return {
			'total_budget': self.total_budget,
			'category_budgets': self.category_budgets,
			'category_expenses': self.category_expenses
		}
