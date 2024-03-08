class Investment:
	def __init__(self):
		self.investments = {}

	def add_investment(self, name, amount, current_value):
		self.investments[name] = {'amount': amount, 'current_value': current_value}

	def track_investment(self, name):
		return self.investments.get(name, 'Investment not found')

	def overview(self):
		return self.investments

	def set_alert(self, name, threshold):
		investment = self.investments.get(name)
		if not investment:
			return 'Investment not found'
		if investment['current_value'] <= threshold:
			return f'Alert! The current value of {name} is below the threshold'
		return 'No alert'
