class Budget:
	def __init__(self):
		self.budget_db = {}

	def set_budget(self, user_id, category, amount):
		if user_id not in self.budget_db:
			self.budget_db[user_id] = {}
		self.budget_db[user_id][category] = {'budget': amount, 'progress': 0}

	def get_budget(self, user_id, category):
		return self.budget_db.get(user_id, {}).get(category, None)

	def update_progress(self, user_id, category, amount):
		budget = self.get_budget(user_id, category)
		if budget:
			budget['progress'] += amount
			if budget['progress'] >= budget['budget']:
				return 'Budget limit exceeded'
			elif budget['progress'] >= 0.9 * budget['budget']:
				return 'Budget limit nearing'
			else:
				return 'Budget update successful'
		else:
			return 'No budget set for this category'
