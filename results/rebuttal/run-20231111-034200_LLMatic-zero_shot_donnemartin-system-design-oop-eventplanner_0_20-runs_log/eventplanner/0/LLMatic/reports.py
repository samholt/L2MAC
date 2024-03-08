class Reports:
	def __init__(self):
		self.reports = {}

	def generate_report(self, event_id):
		# Mocking event success metrics
		self.reports[event_id] = {
			'attendees': 100,
			'feedback': [],
			'revenue': 1000
		}
		return self.reports[event_id]

	def collect_feedback(self, event_id, feedback):
		if event_id in self.reports:
			self.reports[event_id]['feedback'].append(feedback)
			return True
		return False
