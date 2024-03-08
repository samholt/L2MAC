import pytest
import reporting

def test_import():
	assert reporting is not None

def test_report_generation():
	report = reporting.Report('event1')
	metrics = report.generate_report()
	assert metrics == {'attendance': 100, 'engagement': 75, 'satisfaction': 80}

def test_feedback_collection():
	report = reporting.Report('event1')
	feedback = report.collect_feedback('Great event!')
	assert feedback == ['Great event!']
