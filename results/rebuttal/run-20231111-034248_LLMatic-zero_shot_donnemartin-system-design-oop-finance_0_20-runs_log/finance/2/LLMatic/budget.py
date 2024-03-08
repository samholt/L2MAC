class Budget:
	def __init__(self):
		self.budgets = {}

	def set_monthly_budget(self, user_id, amount):
		self.budgets[user_id] = {'monthly_budget': amount, 'spent': 0}

	def add_expense(self, user_id, amount):
		self.budgets[user_id]['spent'] += amount
		if self.budgets[user_id]['spent'] >= self.budgets[user_id]['monthly_budget']:
			return 'Budget limit exceeded'
		elif self.budgets[user_id]['spent'] >= 0.9 * self.budgets[user_id]['monthly_budget']:
			return 'Budget limit nearing'
		else:
			return 'Expense added'

	def get_budget_status(self, user_id):
		return self.budgets[user_id]
