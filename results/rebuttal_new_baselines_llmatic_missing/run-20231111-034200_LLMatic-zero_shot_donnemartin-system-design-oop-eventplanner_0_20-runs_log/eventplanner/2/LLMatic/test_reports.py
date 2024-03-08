import pytest
from reports import Reports

def test_add_report():
	reports = Reports()
	reports.add_report('event1', 'High', 'Good')
	assert reports.get_report('event1') == {'success_metric': 'High', 'feedback': 'Good'}

def test_get_report():
	reports = Reports()
	reports.add_report('event1', 'High', 'Good')
	assert reports.get_report('event1') == {'success_metric': 'High', 'feedback': 'Good'}
	assert reports.get_report('event2') == None

def test_get_all_reports():
	reports = Reports()
	reports.add_report('event1', 'High', 'Good')
	reports.add_report('event2', 'Medium', 'Average')
	assert reports.get_all_reports() == {'event1': {'success_metric': 'High', 'feedback': 'Good'}, 'event2': {'success_metric': 'Medium', 'feedback': 'Average'}}
