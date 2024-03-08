import pytest
from reporting import Reporting

def test_generate_and_view_report():
	reporting = Reporting()
	reporting.generate_report('event1', 'success metrics', 'feedback')
	report = reporting.view_report('event1')
	assert report.event_id == 'event1'
	assert report.success_metrics == 'success metrics'
	assert report.feedback == 'feedback'

	report = reporting.view_report('event2')
	assert report == 'No report found for this event.'
