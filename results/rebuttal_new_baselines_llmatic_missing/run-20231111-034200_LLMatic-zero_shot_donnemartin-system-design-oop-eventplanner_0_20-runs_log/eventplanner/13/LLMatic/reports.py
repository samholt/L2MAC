class Report:
	def __init__(self):
		self.reports = {}

	def generate_report(self, report_id, report_data):
		self.reports[report_id] = report_data
		return True

	def get_report(self, report_id):
		return self.reports.get(report_id, None)

	def collect_feedback(self, report_id, feedback):
		report = self.reports.get(report_id)
		if report is None:
			return False
		report['feedback'] = feedback
		return True
