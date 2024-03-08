class Budget:
	def __init__(self):
		self.budget_goals = {}
		self.spending_patterns = {}

	def set_adjust_budget(self, user_id, budget):
		self.budget_goals[user_id] = budget

	def alert_budget_limit(self, user_id):
		message = self._get_budget_message(user_id)
		if message:
			return message
		else:
			return 'No budget or spending data available'

	def analyze_spending(self, user_id):
		message = self._get_budget_message(user_id)
		if message:
			return 'Suggestion: Consider adjusting your budget'
		else:
			return 'No budget or spending data available'

	def _get_budget_message(self, user_id):
		if user_id in self.spending_patterns and user_id in self.budget_goals:
			if self.spending_patterns[user_id] >= self.budget_goals[user_id]:
				return 'Alert: You have reached your budget limit'
			else:
				return 'You are within your budget limit'
