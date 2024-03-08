class ReportsAlerts:
	def __init__(self):
		self.reports = {}
		self.alerts = {}

	def generate_report(self, user_id, report):
		self.reports[user_id] = report
		return self.reports[user_id]

	def custom_alert(self, user_id, alert):
		self.alerts[user_id] = alert
		return self.alerts[user_id]
