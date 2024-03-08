report_db = {}

def generate_report(event_id):
	return report_db.get(event_id, 'No report found')

def collect_feedback(event_id, feedback):
	if event_id in report_db:
		report_db[event_id]['feedback'].append(feedback)
	else:
		report_db[event_id] = {'feedback': [feedback]}
	return 'Feedback collected'
