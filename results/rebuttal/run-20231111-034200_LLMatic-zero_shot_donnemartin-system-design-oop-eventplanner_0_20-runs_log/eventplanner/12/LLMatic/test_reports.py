import pytest
from reports import Reports

def test_generate_report():
	reports = Reports()
	report = reports.generate_report('event_1')
	assert report['event_id'] == 'event_1'
	assert report['success_metric'] == 85
	assert report['feedback'] == []

def test_collect_feedback():
	reports = Reports()
	reports.generate_report('event_1')
	is_feedback_collected = reports.collect_feedback('event_1', 'Great event!')
	assert is_feedback_collected == True
	assert 'Great event!' in reports.reports_data['event_1']['feedback']
