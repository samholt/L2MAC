class Investment:
	def __init__(self, value, roi, alerts):
		self.value = value
		self.roi = roi
		self.alerts = alerts

	def add_investment(self, amount):
		self.value += amount

	def calculate_roi(self):
		return self.value * self.roi

	def set_alert(self, alert):
		self.alerts.append(alert)
