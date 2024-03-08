class Report:
	def __init__(self):
		self.reports_db = {}

	def generate_report(self, event_id):
		# Mock implementation of report generation
		report = {'event_id': event_id, 'success_metric': 80, 'feedback': []}
		self.reports_db[event_id] = report
		return report

	def collect_feedback(self, event_id, feedback):
		# Mock implementation of feedback collection
		if event_id in self.reports_db:
			self.reports_db[event_id]['feedback'].append(feedback)
		return self.reports_db[event_id]
