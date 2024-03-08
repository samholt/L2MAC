class Budget:
	def __init__(self):
		self.budget_data = {}

	def set_budget(self, event_id, budget):
		self.budget_data[event_id] = {'total': budget, 'spent': 0, 'categories': {}}

	def track_budget(self, event_id, category, amount):
		if event_id not in self.budget_data:
			return 'Event not found'
		if category not in self.budget_data[event_id]['categories']:
			self.budget_data[event_id]['categories'][category] = amount
		else:
			self.budget_data[event_id]['categories'][category] += amount
		self.budget_data[event_id]['spent'] += amount

	def get_budget_status(self, event_id):
		if event_id not in self.budget_data:
			return 'Event not found'
		return self.budget_data[event_id]

	def check_budget_overrun(self, event_id):
		if event_id not in self.budget_data:
			return 'Event not found'
		if self.budget_data[event_id]['spent'] > self.budget_data[event_id]['total']:
			return 'Budget overrun'
		return 'Within budget'
