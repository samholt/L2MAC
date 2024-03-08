class Reporting:
	def __init__(self):
		self.reports = {}
		self.feedback = {}

	def generate_report(self, event_id, success_metrics):
		self.reports[event_id] = success_metrics
		return self.reports[event_id]

	def collect_feedback(self, event_id, feedback):
		if event_id not in self.feedback:
			self.feedback[event_id] = []
		self.feedback[event_id].append(feedback)
		return self.feedback[event_id]
