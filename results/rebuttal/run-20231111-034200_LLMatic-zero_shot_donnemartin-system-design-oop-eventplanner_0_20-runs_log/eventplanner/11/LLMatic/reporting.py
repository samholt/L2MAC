class Reporting:
	def __init__(self):
		self.event_reports = {}
		self.feedback_reports = {}

	def generate_event_report(self, event_id):
		# Mocking event success metrics
		self.event_reports[event_id] = {'attendees': 100, 'engagement': 75, 'satisfaction': 80}
		return self.event_reports[event_id]

	def collect_feedback(self, event_id, feedback):
		# Mocking feedback collection
		if event_id not in self.feedback_reports:
			self.feedback_reports[event_id] = []
		self.feedback_reports[event_id].append(feedback)
		return self.feedback_reports[event_id]
