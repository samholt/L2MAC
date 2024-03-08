class Budget:
	def __init__(self, monthly_budget):
		self.monthly_budget = monthly_budget
		self.current_spending = 0

	def set_budget(self, new_budget):
		# Set the budget
		self.monthly_budget = new_budget

	def adjust_budget(self, adjustment):
		# Adjust the budget
		self.monthly_budget += adjustment

	def alert_user(self):
		# Alert the user if they are nearing their budget limit
		if self.current_spending >= self.monthly_budget * 0.9:
			return 'You are nearing your budget limit.'
		else:
			return 'You are within your budget limit.'

	def analyze_spending(self, spending_history):
		# Analyze the user's spending
		average_spending = sum(spending_history) / len(spending_history)
		if average_spending > self.monthly_budget:
			return 'Consider adjusting your budget.'
		else:
			return 'Your budget is appropriate.'
