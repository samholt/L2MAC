class Reporting:
	def __init__(self):
		self.feedback = {}
		self.reports = {}

	def collect_feedback(self, event_id, user_id, feedback):
		if event_id not in self.feedback:
			self.feedback[event_id] = {}
		self.feedback[event_id][user_id] = feedback

	def generate_report(self, event_id):
		if event_id in self.feedback:
			self.reports[event_id] = {
				'average_rating': sum(self.feedback[event_id].values()) / len(self.feedback[event_id]),
				'feedback_count': len(self.feedback[event_id])
			}
		return self.reports.get(event_id, {})
