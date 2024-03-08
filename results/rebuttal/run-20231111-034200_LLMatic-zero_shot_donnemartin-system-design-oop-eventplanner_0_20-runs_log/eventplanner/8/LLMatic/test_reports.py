from reports import Report

def test_report_generation():
	report = Report()
	generated_report = report.generate_report('event_1')
	assert generated_report['event_id'] == 'event_1'
	assert generated_report['success_metric'] == 80
	assert generated_report['feedback'] == []

def test_feedback_collection():
	report = Report()
	report.generate_report('event_1')
	report.collect_feedback('event_1', 'Great event!')
	assert report.reports_db['event_1']['feedback'] == ['Great event!']
