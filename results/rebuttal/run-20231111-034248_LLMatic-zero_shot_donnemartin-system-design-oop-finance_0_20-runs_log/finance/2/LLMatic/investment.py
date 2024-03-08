class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, user_id, investment_name, investment_value):
		if user_id not in self.investments:
			self.investments[user_id] = {}
		self.investments[user_id][investment_name] = investment_value

	def get_investment(self, user_id, investment_name):
		return self.investments.get(user_id, {}).get(investment_name, 0)

	def get_total_investment(self, user_id):
		return sum(self.investments.get(user_id, {}).values())

	def set_alert(self, user_id, investment_name, alert_value):
		if user_id not in self.investments:
			return 'User does not have any investments'
		if investment_name not in self.investments[user_id]:
			return 'Investment not found'
		self.investments[user_id][investment_name] = {'alert': alert_value}
		return 'Alert set successfully'
