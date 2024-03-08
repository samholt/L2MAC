class Reports:
	def __init__(self):
		self.reports = {}

	def add_report(self, event_id, success_metric, feedback):
		if event_id not in self.reports:
			self.reports[event_id] = {'success_metric': success_metric, 'feedback': feedback}
		else:
			self.reports[event_id]['success_metric'].append(success_metric)
			self.reports[event_id]['feedback'].append(feedback)

	def get_report(self, event_id):
		return self.reports.get(event_id, None)

	def get_all_reports(self):
		return self.reports
