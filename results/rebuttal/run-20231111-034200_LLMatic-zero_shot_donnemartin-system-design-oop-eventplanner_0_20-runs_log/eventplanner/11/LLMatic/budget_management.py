class BudgetManagement:
	def __init__(self):
		self.budgets = {}

	def set_budget(self, event_id, budget):
		self.budgets[event_id] = {'budget': budget, 'spent': 0}

	def track_budget(self, event_id, amount):
		if event_id in self.budgets:
			self.budgets[event_id]['spent'] += amount

	def get_budget_status(self, event_id):
		if event_id in self.budgets:
			budget = self.budgets[event_id]['budget']
			spent = self.budgets[event_id]['spent']
			return {'budget': budget, 'spent': spent, 'remaining': budget - spent}
		else:
			return None

	def check_budget_overrun(self, event_id):
		status = self.get_budget_status(event_id)
		if status and status['remaining'] < 0:
			return True
		else:
			return False
