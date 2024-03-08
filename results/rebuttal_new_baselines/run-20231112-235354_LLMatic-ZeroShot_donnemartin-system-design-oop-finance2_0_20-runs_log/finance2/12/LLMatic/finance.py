class Finance:
	def __init__(self):
		self.expenses = {}
		self.incomes = {}
		self.expense_categories = {}
		self.income_categories = {}

	def add_expense(self, user_id, expense):
		if user_id not in self.expenses:
			self.expenses[user_id] = []
		self.expenses[user_id].append(expense)

	def add_income(self, user_id, income):
		if user_id not in self.incomes:
			self.incomes[user_id] = []
		self.incomes[user_id].append(income)

	def import_expenses(self, user_id, expenses):
		if user_id not in self.expenses:
			self.expenses[user_id] = []
		self.expenses[user_id].extend(expenses)

	def import_incomes(self, user_id, incomes):
		if user_id not in self.incomes:
			self.incomes[user_id] = []
		self.incomes[user_id].extend(incomes)

	def categorize_expense(self, user_id, expense, category):
		if user_id not in self.expense_categories:
			self.expense_categories[user_id] = {}
		self.expense_categories[user_id][expense] = category

	def categorize_income(self, user_id, income, category):
		if user_id not in self.income_categories:
			self.income_categories[user_id] = {}
		self.income_categories[user_id][income] = category
