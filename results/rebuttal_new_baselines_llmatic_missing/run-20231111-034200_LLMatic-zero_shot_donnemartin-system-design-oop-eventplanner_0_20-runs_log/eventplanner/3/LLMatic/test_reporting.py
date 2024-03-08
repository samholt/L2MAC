import pytest
import reporting

def test_generate_report():
	report = reporting.generate_report('event1', {'attendance': 100}, ['Great event!'])
	assert report.event_id == 'event1'
	assert report.success_metrics == {'attendance': 100}
	assert report.feedback == ['Great event!']

def test_collect_feedback():
	reporting.generate_report('event2', {'attendance': 200}, [])
	assert reporting.collect_feedback('event2', 'Awesome event!') == True
	assert 'Awesome event!' in reporting.mock_db['event2'].feedback
