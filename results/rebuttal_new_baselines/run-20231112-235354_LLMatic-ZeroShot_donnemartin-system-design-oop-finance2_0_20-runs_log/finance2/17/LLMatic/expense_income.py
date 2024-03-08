class Expense:
	def __init__(self):
		self.expenses = {}

	def import_expenses(self, expenses):
		for expense in expenses:
			self.expenses[expense['name']] = expense['amount']

	def categorize_expenses(self, categories):
		self.expenses = {}
		for category in categories:
			self.expenses[category['name']] = category['amount']

	def visualize_expenses(self):
		return self.expenses


class Income:
	def __init__(self):
		self.incomes = {}

	def import_incomes(self, incomes):
		for income in incomes:
			self.incomes[income['name']] = income['amount']

	def categorize_incomes(self, categories):
		self.incomes = {}
		for category in categories:
			self.incomes[category['name']] = category['amount']

	def visualize_incomes(self):
		return self.incomes
