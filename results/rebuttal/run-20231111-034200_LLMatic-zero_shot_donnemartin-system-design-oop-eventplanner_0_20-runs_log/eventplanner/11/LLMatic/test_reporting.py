import pytest
from reporting import Reporting

def test_generate_event_report():
	reporting = Reporting()
	report = reporting.generate_event_report('event1')
	assert report == {'attendees': 100, 'engagement': 75, 'satisfaction': 80}

def test_collect_feedback():
	reporting = Reporting()
	feedback = reporting.collect_feedback('event1', 'Great event!')
	assert feedback == ['Great event!']
