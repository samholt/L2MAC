class Report:
	def __init__(self, event_id, success_metrics, feedback):
		self.event_id = event_id
		self.success_metrics = success_metrics
		self.feedback = feedback


class Reporting:
	def __init__(self):
		self.reports = {}

	def generate_report(self, event_id, success_metrics, feedback):
		report = Report(event_id, success_metrics, feedback)
		self.reports[event_id] = report

	def view_report(self, event_id):
		if event_id in self.reports:
			return self.reports[event_id]
		else:
			return 'No report found for this event.'
