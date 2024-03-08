class Report:
	def __init__(self):
		self.event_metrics = {}
		self.feedback = {}

	def generate_report(self, event_id):
		# Mock implementation of report generation
		self.event_metrics[event_id] = {'attendees': 100, 'duration': 3, 'satisfaction': 4.5}
		return self.event_metrics[event_id]

	def collect_feedback(self, event_id, feedback):
		# Mock implementation of feedback collection
		self.feedback[event_id] = feedback
		return self.feedback[event_id]
