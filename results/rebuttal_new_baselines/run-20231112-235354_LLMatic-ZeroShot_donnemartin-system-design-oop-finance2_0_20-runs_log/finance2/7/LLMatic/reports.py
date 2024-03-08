class Reports:
	def __init__(self):
		self.reports = {}

	def generate_monthly_summary(self, user):
		# Mock implementation of generating monthly summary
		self.reports['monthly_summary'] = 'Monthly summary for user: ' + user.username

	def generate_alerts(self, user):
		# Mock implementation of generating alerts
		self.reports['alerts'] = 'Alerts for user: ' + user.username

	def get_report(self, report_type):
		return self.reports.get(report_type, 'No such report')
