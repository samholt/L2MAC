class Budget:
	def __init__(self):
		self.budgets = {}

	def set_budget(self, event_id, amount):
		self.budgets[event_id] = {'budget': amount, 'spent': 0}

	def track_budget(self, event_id, amount):
		if event_id in self.budgets:
			self.budgets[event_id]['spent'] += amount
			return True
		return False

	def alert_overrun(self, event_id):
		if event_id in self.budgets:
			if self.budgets[event_id]['spent'] > self.budgets[event_id]['budget']:
				return 'Budget overrun'
			return 'Budget is under control'
		return 'Event not found'
