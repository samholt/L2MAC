class Budget:
	def __init__(self, user):
		self.user = user
		self.categories = {}
		self.goals = {}

	def set_budget(self, category, amount):
		self.categories[category] = amount
		return 'Budget set successfully'

	def alert_user(self, category):
		total_expense = sum([transaction.amount for transaction in self.user.transactions if transaction.category == category and transaction.type == 'expense'])
		if total_expense >= self.categories[category]:
			return 'Alert! You have reached or exceeded your budget limit for ' + category
		else:
			return 'You are nearing your budget limit for ' + category

	def track_progress(self, goal):
		if self.user.balance >= self.goals[goal]:
			return 'Congratulations! You have reached your financial goal for ' + goal
		else:
			return 'You are ' + str(self.goals[goal] - self.user.balance) + ' away from your financial goal for ' + goal
