import pytest
from reports import Report
from database import Database

def test_report_generation():
	report = Report('event1', {'attendance': 100, 'engagement': 90}, 'Great event!')
	assert report.generate_report() == {'event_id': 'event1', 'success_metrics': {'attendance': 100, 'engagement': 90}, 'feedback': 'Great event!'}

def test_report_viewing():
	report = Report('event1', {'attendance': 100, 'engagement': 90}, 'Great event!')
	assert report.view_report() == {'event_id': 'event1', 'success_metrics': {'attendance': 100, 'engagement': 90}, 'feedback': 'Great event!'}

def test_report_storage():
	db = Database()
	report = Report('event1', {'attendance': 100, 'engagement': 90}, 'Great event!')
	db.add_report('report1', report)
	assert db.get_report('report1') == report
