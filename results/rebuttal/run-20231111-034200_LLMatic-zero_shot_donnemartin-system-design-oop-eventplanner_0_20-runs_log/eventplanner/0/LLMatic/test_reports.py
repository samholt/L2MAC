import pytest
from reports import Reports

def test_generate_report():
	reports = Reports()
	report = reports.generate_report('event1')
	assert report == {'attendees': 100, 'feedback': [], 'revenue': 1000}

def test_collect_feedback():
	reports = Reports()
	reports.generate_report('event1')
	assert reports.collect_feedback('event1', 'Great event!') == True
	assert reports.collect_feedback('event2', 'Great event!') == False
