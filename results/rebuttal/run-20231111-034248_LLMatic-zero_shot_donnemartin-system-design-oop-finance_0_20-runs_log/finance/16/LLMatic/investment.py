class Investment:
	def __init__(self):
		self.portfolios = {}

	def add_portfolio(self, name, initial_investment):
		self.portfolios[name] = {'investment': initial_investment, 'value': initial_investment}

	def track_portfolio(self, name, new_value):
		if name in self.portfolios:
			self.portfolios[name]['value'] = new_value

	def overview(self):
		total_investment = sum([portfolio['investment'] for portfolio in self.portfolios.values()])
		total_value = sum([portfolio['value'] for portfolio in self.portfolios.values()])
		return {'total_investment': total_investment, 'total_value': total_value, 'profit': total_value - total_investment}

	def set_alert(self, name, threshold):
		if name in self.portfolios:
			self.portfolios[name]['alert'] = threshold
