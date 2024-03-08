import pytest
from reports import Report

@pytest.fixture
def report_manager():
	report_manager = Report()
	report_manager.generate_report('1', {'title': 'Test Report', 'content': 'This is a test report'})
	return report_manager

def test_generate_report(report_manager):
	assert report_manager.generate_report('2', {'title': 'Test Report 2', 'content': 'This is another test report'})
	assert report_manager.get_report('2') == {'title': 'Test Report 2', 'content': 'This is another test report'}

def test_get_report(report_manager):
	assert report_manager.get_report('1') == {'title': 'Test Report', 'content': 'This is a test report'}
	assert report_manager.get_report('2') is None

def test_collect_feedback(report_manager):
	assert report_manager.collect_feedback('1', 'This is feedback')
	assert report_manager.get_report('1') == {'title': 'Test Report', 'content': 'This is a test report', 'feedback': 'This is feedback'}
	assert not report_manager.collect_feedback('2', 'This is feedback')
