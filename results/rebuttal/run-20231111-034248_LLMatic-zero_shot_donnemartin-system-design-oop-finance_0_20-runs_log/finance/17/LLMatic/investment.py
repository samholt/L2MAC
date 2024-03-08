class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, name, amount_invested, current_value):
		self.investments[name] = {'amount_invested': amount_invested, 'current_value': current_value}

	def get_investment_overview(self):
		return self.investments

	def alert_significant_change(self, name, new_value):
		if name in self.investments:
			old_value = self.investments[name]['current_value']
			change_percentage = ((new_value - old_value) / old_value) * 100
			if abs(change_percentage) > 10:
				return f'Significant change in {name} investment: {round(change_percentage, 2)}%'
			else:
				return 'No significant change'
		else:
			return 'Investment not found'
