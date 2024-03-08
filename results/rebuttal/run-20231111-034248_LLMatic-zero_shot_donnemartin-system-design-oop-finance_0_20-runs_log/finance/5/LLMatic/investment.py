class Investment:
	def __init__(self, investment_name, investment_type, amount_invested, current_value, roi):
		self.investment_name = investment_name
		self.investment_type = investment_type
		self.amount_invested = amount_invested
		self.current_value = current_value
		self.roi = roi

	def add_investment(self, investment_name, investment_type, amount_invested):
		self.investment_name = investment_name
		self.investment_type = investment_type
		self.amount_invested = amount_invested
		self.current_value = amount_invested
		self.roi = 0

	def track_investment(self, current_value):
		self.current_value = current_value
		self.roi = (current_value - self.amount_invested) / self.amount_invested

	def alert_user(self):
		if self.roi >= 0.2:
			return 'Investment value has increased significantly'
		elif self.roi <= -0.2:
			return 'Investment value has decreased significantly'
		else:
			return 'Investment value is stable'
