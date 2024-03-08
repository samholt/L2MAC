class Expense:
	def __init__(self, amount, category, date):
		self.amount = amount
		self.category = category
		self.date = date

	def import_expenses(self, expenses):
		# This function will import expenses
		pass

	def categorize_expense(self):
		# This function will categorize the expense
		pass

	def visualize_expense_history(self):
		# This function will visualize the expense history
		pass


class Income:
	def __init__(self, amount, source, date):
		self.amount = amount
		self.source = source
		self.date = date

	def import_incomes(self, incomes):
		# This function will import incomes
		pass

	def categorize_income(self):
		# This function will categorize the income
		pass

	def visualize_income_history(self):
		# This function will visualize the income history
		pass


class Budget:
	def __init__(self, amount):
		self.amount = amount
		self.spent = 0

	def adjust_budget(self, adjustment):
		self.amount += adjustment

	def add_expense(self, expense):
		self.spent += expense.amount

	def check_budget(self):
		remaining = self.amount - self.spent
		if remaining < 0.1 * self.amount:
			return 'Warning: You are nearing your budget limit'
		else:
			return 'You are within your budget'

