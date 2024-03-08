class Report:
	def __init__(self, event_id):
		self.event_id = event_id
		self.success_metrics = {}
		self.feedback = []

	def generate_report(self):
		# Mock implementation of report generation
		self.success_metrics = {'attendance': 100, 'engagement': 75, 'satisfaction': 80}
		return self.success_metrics

	def collect_feedback(self, feedback):
		# Mock implementation of feedback collection
		self.feedback.append(feedback)
		return self.feedback
