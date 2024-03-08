class Investment:
	def __init__(self):
		self.investment_db = {}

	def add_investment(self, user_id, investment_name, current_value, return_on_investment):
		if user_id not in self.investment_db:
			self.investment_db[user_id] = []
		self.investment_db[user_id].append({
			'investment_name': investment_name,
			'current_value': current_value,
			'return_on_investment': return_on_investment
		})

	def get_investment_overview(self, user_id):
		if user_id in self.investment_db:
			return self.investment_db[user_id]
		return []

	def set_investment_alert(self, user_id, investment_name, alert_value):
		for investment in self.investment_db.get(user_id, []):
			if investment['investment_name'] == investment_name:
				investment['alert_value'] = alert_value
				return 'Alert set successfully'
		return 'Investment not found'
