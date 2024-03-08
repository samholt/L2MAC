class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, user_id, investment):
		if user_id not in self.investments:
			self.investments[user_id] = []
		self.investments[user_id].append(investment)
		return {'status': 'success', 'message': 'Investment added successfully'}

	def track_investment(self, user_id):
		if user_id in self.investments:
			return {'status': 'success', 'data': self.investments[user_id]}
		else:
			return {'status': 'error', 'message': 'No investments found for this user'}

	def calculate_performance(self, user_id):
		if user_id in self.investments:
			total_investment = sum([investment['amount'] for investment in self.investments[user_id]])
			total_value = sum([investment['current_value'] for investment in self.investments[user_id]])
			return {'status': 'success', 'data': {'total_investment': total_investment, 'total_value': total_value, 'performance': (total_value - total_investment) / total_investment}}
		else:
			return {'status': 'error', 'message': 'No investments found for this user'}

	def set_alert(self, user_id, investment_id, alert_value):
		for investment in self.investments.get(user_id, []):
			if investment['id'] == investment_id:
				investment['alert_value'] = alert_value
				return {'status': 'success', 'message': 'Alert set successfully'}
		return {'status': 'error', 'message': 'Investment not found'}
