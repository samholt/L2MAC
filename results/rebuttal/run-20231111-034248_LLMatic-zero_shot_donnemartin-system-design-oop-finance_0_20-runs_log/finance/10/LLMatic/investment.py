class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, name, amount):
		self.investments[name] = amount

	def track_investment(self, name, new_value):
		old_value = self.investments.get(name, 0)
		return (new_value - old_value) / old_value if old_value else 0

	def alert_significant_change(self, name, new_value):
		change = self.track_investment(name, new_value)
		if abs(change) > 0.1:
			return f'Significant change in {name}! Change: {change * 100}%'
		return 'No significant change.'
