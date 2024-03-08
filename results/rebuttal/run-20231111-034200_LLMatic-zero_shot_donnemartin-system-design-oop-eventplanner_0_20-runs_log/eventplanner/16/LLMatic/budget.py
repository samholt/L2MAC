class Budget:
	def __init__(self):
		self.budgets = {}

	def set_budget(self, event_id, total_budget, breakdown):
		self.budgets[event_id] = {'total_budget': total_budget, 'breakdown': breakdown, 'spent': 0}

	def track_budget(self, event_id, amount):
		self.budgets[event_id]['spent'] += amount
		if self.budgets[event_id]['spent'] > self.budgets[event_id]['total_budget']:
			return 'Budget overrun'
		return 'Budget is within limit'

	def get_budget(self, event_id):
		return self.budgets.get(event_id, 'No budget set for this event')

