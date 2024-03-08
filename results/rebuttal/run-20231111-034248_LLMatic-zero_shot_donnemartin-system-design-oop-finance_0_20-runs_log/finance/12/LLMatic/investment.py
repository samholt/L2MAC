class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, name, amount, current_value):
		self.investments[name] = {'amount': amount, 'current_value': current_value}

	def get_investment_overview(self):
		return self.investments

	def set_alert(self, name, threshold):
		if name in self.investments:
			if self.investments[name]['current_value'] < threshold:
				return f'Alert: Your investment in {name} has fallen below the threshold'
			else:
				return f'Your investment in {name} is safe'
		else:
			return f'No investment found with the name {name}'
