class Budget:
	def __init__(self):
		self.budget_data = {}

	def set_monthly_budget(self, user_id, amount):
		self.budget_data[user_id] = {'monthly_budget': amount, 'current_spending': 0}

	def add_expense(self, user_id, amount):
		self.budget_data[user_id]['current_spending'] += amount
		self.check_budget_status(user_id)

	def check_budget_status(self, user_id):
		budget_info = self.budget_data[user_id]
		if budget_info['current_spending'] > budget_info['monthly_budget']:
			print(f'User {user_id} has exceeded the monthly budget.')
			self.budget_data[user_id]['current_spending'] = 0
		elif budget_info['current_spending'] > 0.9 * budget_info['monthly_budget']:
			print(f'User {user_id} is nearing the monthly budget limit.')

	def get_budget_info(self, user_id):
		return self.budget_data[user_id]
