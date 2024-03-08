class Budget:
	def __init__(self):
		self.budgets = {}

	def create_budget(self, user, amount, category):
		budget_id = len(self.budgets) + 1
		self.budgets[budget_id] = {'user': user, 'amount': amount, 'category': category}
		return budget_id

	def get_user_budgets(self, user):
		return [budget for budget_id, budget in self.budgets.items() if budget['user'] == user]

	def adjust_budget(self, budget_id, amount):
		if budget_id in self.budgets:
			self.budgets[budget_id]['amount'] = amount
			return True
		return False
