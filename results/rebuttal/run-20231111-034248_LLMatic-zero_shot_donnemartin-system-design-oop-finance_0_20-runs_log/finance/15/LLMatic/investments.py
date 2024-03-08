class Investment:
	def __init__(self):
		self.portfolios = {}

	def add_portfolio(self, name, initial_investment):
		if name in self.portfolios:
			return 'Portfolio already exists.'
		self.portfolios[name] = {'investment': initial_investment, 'value': initial_investment}
		return 'Portfolio added successfully.'

	def track_portfolio(self, name, current_value):
		if name not in self.portfolios:
			return 'Portfolio does not exist.'
		self.portfolios[name]['value'] = current_value
		return 'Portfolio updated successfully.'

	def overview(self):
		return self.portfolios

	def set_alert(self, name, threshold):
		if name not in self.portfolios:
			return 'Portfolio does not exist.'
		self.portfolios[name]['alert'] = threshold
		return 'Alert set successfully.'

	def check_alerts(self):
		alerts = []
		for name, portfolio in self.portfolios.items():
			if 'alert' in portfolio and portfolio['value'] <= portfolio['alert']:
				alerts.append(f'{name} has reached the alert threshold.')
		return alerts
