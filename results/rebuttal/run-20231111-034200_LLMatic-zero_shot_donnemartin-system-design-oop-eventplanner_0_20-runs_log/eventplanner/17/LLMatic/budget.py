class Budget:
	def __init__(self):
		self.budget_data = {}

	def set_budget(self, event_id, budget):
		self.budget_data[event_id] = {'budget': budget, 'spent': 0}

	def track_budget(self, event_id, amount):
		if event_id in self.budget_data:
			self.budget_data[event_id]['spent'] += amount
			if self.budget_data[event_id]['spent'] > self.budget_data[event_id]['budget']:
				return 'Budget overrun'
			else:
				return 'Budget is under control'
		else:
			return 'Event not found'

	def get_budget_status(self, event_id):
		if event_id in self.budget_data:
			return self.budget_data[event_id]
		else:
			return 'Event not found'
