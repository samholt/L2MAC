class ExpenseIncome:
	def __init__(self):
		self.expenses = {}
		self.incomes = {}

	def import_expenses_incomes(self, user, expenses, incomes):
		self.expenses[user] = expenses
		self.incomes[user] = incomes

	def categorize_expenses_incomes(self, user, expense_categories, income_categories):
		self.expenses[user] = {category: self.expenses[user][category] for category in expense_categories}
		self.incomes[user] = {category: self.incomes[user][category] for category in income_categories}

	def visualize_expense_income_history(self, user):
		return {'expenses': self.expenses[user], 'incomes': self.incomes[user]}
