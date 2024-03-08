class Report:
	def __init__(self):
		self.reports = {}
		self.feedback = {}

	def generate_report(self, event_id, success_metrics):
		self.reports[event_id] = success_metrics

	def collect_feedback(self, event_id, feedback):
		self.feedback[event_id] = feedback

	def get_report(self, event_id):
		return self.reports.get(event_id, 'No report found')

	def get_feedback(self, event_id):
		return self.feedback.get(event_id, 'No feedback found')
