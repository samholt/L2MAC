class Reporting:
	def __init__(self):
		self.reports = {}
		self.feedback = {}

	def generate_report(self, event_id, report):
		self.reports[event_id] = report

	def get_report(self, event_id):
		return self.reports.get(event_id, 'No report found')

	def collect_feedback(self, event_id, feedback):
		self.feedback[event_id] = feedback

	def get_feedback(self, event_id):
		return self.feedback.get(event_id, 'No feedback found')

reporting = Reporting()
