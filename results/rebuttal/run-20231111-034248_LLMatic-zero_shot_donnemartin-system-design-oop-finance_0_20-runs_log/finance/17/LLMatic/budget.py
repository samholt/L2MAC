class Budget:
	def __init__(self):
		self.budget_db = {}

	def set_monthly_budget(self, user_id, category, amount):
		if user_id not in self.budget_db:
			self.budget_db[user_id] = {}
		self.budget_db[user_id][category] = {'budget': amount, 'spent': 0}

	def add_expense(self, user_id, category, amount):
		if user_id in self.budget_db and category in self.budget_db[user_id]:
			self.budget_db[user_id][category]['spent'] += amount
			if self.budget_db[user_id][category]['spent'] >= self.budget_db[user_id][category]['budget']:
				return 'Budget limit exceeded!'
			elif self.budget_db[user_id][category]['spent'] >= 0.9 * self.budget_db[user_id][category]['budget']:
				return 'You are nearing your budget limit.'
		return 'Expense added.'

	def get_budget_status(self, user_id, category):
		if user_id in self.budget_db and category in self.budget_db[user_id]:
			return self.budget_db[user_id][category]
		return 'No budget set.'
