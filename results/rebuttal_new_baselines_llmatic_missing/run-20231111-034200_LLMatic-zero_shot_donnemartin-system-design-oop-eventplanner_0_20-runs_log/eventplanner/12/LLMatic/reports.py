class Reports:
	def __init__(self):
		self.reports_data = {}

	def generate_report(self, event_id):
		# Mocking report generation
		report = {'event_id': event_id, 'success_metric': 85, 'feedback': []}
		self.reports_data[event_id] = report
		return report

	def collect_feedback(self, event_id, feedback):
		# Mocking feedback collection
		if event_id in self.reports_data:
			self.reports_data[event_id]['feedback'].append(feedback)
			return True
		return False
