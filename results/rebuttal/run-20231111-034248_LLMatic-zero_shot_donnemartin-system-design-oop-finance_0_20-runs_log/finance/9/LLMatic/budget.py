class Budget:
	def __init__(self, category, limit):
		self.category = category
		self.limit = limit
		self.transactions = []

	def add_transaction(self, transaction):
		self.transactions.append(transaction)

	def get_total_spent(self):
		return sum(transaction.amount for transaction in self.transactions)

	def get_remaining_budget(self):
		return self.limit - self.get_total_spent()

	def is_budget_exceeded(self):
		return self.get_total_spent() > self.limit


class BudgetManager:
	def __init__(self):
		self.budgets = {}

	def add_budget(self, budget):
		self.budgets[budget.category] = budget

	def get_budget(self, category):
		return self.budgets.get(category, None)

	def delete_budget(self, category):
		if category in self.budgets:
			del self.budgets[category]

	def get_all_budgets(self):
		return self.budgets.values()

	def get_total_budget(self):
		return sum(budget.limit for budget in self.get_all_budgets())

	def get_total_spent(self):
		return sum(budget.get_total_spent() for budget in self.get_all_budgets())

	def get_remaining_budget(self):
		return self.get_total_budget() - self.get_total_spent()
