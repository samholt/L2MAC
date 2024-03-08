class Alert:
	def __init__(self, name, threshold):
		self.name = name
		self.threshold = threshold


class Investment:
	def __init__(self, name, quantity, purchase_price, current_price):
		self.name = name
		self.quantity = quantity
		self.purchase_price = purchase_price
		self.current_price = current_price
		self.alerts = []

	def add_alert(self, alert):
		self.alerts.append(alert)

	def track_performance(self):
		return (self.current_price - self.purchase_price) * self.quantity


class InvestmentManager:
	def __init__(self):
		self.investments = {}

	def add_investment(self, name, quantity, purchase_price, current_price):
		investment = Investment(name, quantity, purchase_price, current_price)
		self.investments[name] = investment
		return investment

	def track_investment(self, name):
		investment = self.investments.get(name)
		if investment:
			return investment.track_performance()
		return None

	def set_alert(self, name, alert):
		investment = self.investments.get(name)
		if investment:
			investment.add_alert(alert)
