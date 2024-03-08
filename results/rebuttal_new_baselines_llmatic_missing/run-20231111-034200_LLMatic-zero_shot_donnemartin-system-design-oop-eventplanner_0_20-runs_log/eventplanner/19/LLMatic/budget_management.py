class BudgetManagement:
	def __init__(self):
		self.budget_db = {}

	def set_budget(self, event_id, budget):
		self.budget_db[event_id] = {'total_budget': budget, 'categories': {}, 'spent': 0}

	def add_category(self, event_id, category, budget):
		self.budget_db[event_id]['categories'][category] = {'budget': budget, 'spent': 0}

	def track_spending(self, event_id, category, amount):
		self.budget_db[event_id]['spent'] += amount
		self.budget_db[event_id]['categories'][category]['spent'] += amount

	def check_budget(self, event_id):
		total_budget = self.budget_db[event_id]['total_budget']
		total_spent = self.budget_db[event_id]['spent']
		if total_spent >= total_budget:
			return 'Budget overrun'
		else:
			return 'Budget is under control'

	def breakdown(self, event_id):
		return self.budget_db[event_id]
