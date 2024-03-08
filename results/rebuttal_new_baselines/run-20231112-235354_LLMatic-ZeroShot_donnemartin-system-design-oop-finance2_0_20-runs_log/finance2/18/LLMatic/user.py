class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.expenses = []
		self.incomes = []
		self.budget = None

	def create_account(self):
		# This function will create a new user account
		pass

	def link_bank_account(self):
		# This function will link a bank account
		pass

	def implement_multi_factor_authentication(self):
		# This function will implement multi-factor authentication
		pass

	def add_expense(self, expense):
		self.expenses.append(expense)

	def add_income(self, income):
		self.incomes.append(income)

	def set_budget(self, budget):
		self.budget = budget

	def adjust_budget(self, adjustment):
		self.budget.adjust_budget(adjustment)

	def check_budget(self):
		if self.budget:
			return self.budget.check_budget()
		else:
			return 'No budget set'

