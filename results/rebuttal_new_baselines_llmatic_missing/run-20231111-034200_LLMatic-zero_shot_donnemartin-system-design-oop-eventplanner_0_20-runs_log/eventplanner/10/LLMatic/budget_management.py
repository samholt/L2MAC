from database import Database


class BudgetManagement:
	def __init__(self):
		self.db = Database()
		self.budgets = {}

	def set_budget(self, event_id, total_budget, breakdown):
		self.budgets[event_id] = {'total_budget': total_budget, 'breakdown': breakdown, 'spent': 0}
		self.db.insert(event_id, self.budgets[event_id])

	def track_budget(self, event_id, amount_spent):
		budget = self.db.get(event_id)
		if budget == 'Data not found':
			return 'Budget not found'
		budget['spent'] += amount_spent
		if budget['spent'] > budget['total_budget']:
			return 'Budget overrun'
		self.db.update(event_id, budget)
		return 'Budget updated'

