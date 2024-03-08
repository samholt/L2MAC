class Budget:
	def __init__(self):
		self.budget_db = {}

	def set_budget(self, user_id, category, limit):
		if user_id not in self.budget_db:
			self.budget_db[user_id] = {}
		self.budget_db[user_id][category] = {'limit': limit, 'current_spending': 0}

	def update_spending(self, user_id, category, amount):
		if user_id in self.budget_db and category in self.budget_db[user_id]:
			self.budget_db[user_id][category]['current_spending'] += amount

	def get_budget_status(self, user_id):
		if user_id in self.budget_db:
			return self.budget_db[user_id]
		return {}

