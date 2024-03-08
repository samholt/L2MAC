import pytest
from reports import Report

def test_generate_report():
	report = Report()
	report.generate_report('event1', {'attendance': 100, 'satisfaction': 90})
	assert report.get_report('event1') == {'attendance': 100, 'satisfaction': 90}

def test_collect_feedback():
	report = Report()
	report.collect_feedback('event1', 'Great event!')
	assert report.get_feedback('event1') == 'Great event!'
