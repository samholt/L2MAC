class Report:
	def __init__(self, event_id, success_metrics, feedback):
		self.event_id = event_id
		self.success_metrics = success_metrics
		self.feedback = feedback

mock_db = {}

def generate_report(event_id, success_metrics, feedback):
	report = Report(event_id, success_metrics, feedback)
	mock_db[event_id] = report
	return report

def collect_feedback(event_id, feedback):
	if event_id in mock_db:
		mock_db[event_id].feedback.append(feedback)
		return True
	return False
