import reporting

def test_import():
	assert reporting is not None

def test_generate_report():
	report = reporting.Report()
	data = report.generate_report('event1')
	assert data['success_metrics'] == 'High'
	assert data['feedback'] == 'Positive'

def test_collect_feedback():
	report = reporting.Report()
	data = report.generate_report('event1')
	updated_data = report.collect_feedback('event1', 'Neutral')
	assert updated_data['feedback'] == 'Neutral'
