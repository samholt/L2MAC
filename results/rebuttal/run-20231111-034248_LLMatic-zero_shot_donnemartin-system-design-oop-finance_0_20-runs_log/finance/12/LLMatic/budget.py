class Budget:
	def __init__(self):
		self.budget_db = {}

	def set_monthly_budget(self, user_id, category, amount):
		if user_id not in self.budget_db:
			self.budget_db[user_id] = {}
		self.budget_db[user_id][category] = {'budget': amount, 'progress': 0}

	def get_budget_status(self, user_id, category):
		if user_id in self.budget_db and category in self.budget_db[user_id]:
			budget_info = self.budget_db[user_id][category]
			if budget_info['progress'] >= budget_info['budget']:
				return 'You have exceeded your budget for this category.'
			elif budget_info['progress'] >= 0.9 * budget_info['budget']:
				return 'You are nearing your budget limit for this category.'
			else:
				return 'You are within your budget for this category.'
		else:
			return 'No budget set for this category.'

	def update_budget_progress(self, user_id, category, amount):
		if user_id in self.budget_db and category in self.budget_db[user_id]:
			self.budget_db[user_id][category]['progress'] += amount
