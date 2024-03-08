import pytest
from report import Report, ReportManager
from user import User
from investment import Investment


def test_report():
	user = User('test_user', 'password', 'test_user@example.com')
	investment = Investment('test_investment', 10, 100, 150)
	report = Report(user, 'January', 5000, 2000, 1000, [investment])

	assert report.generate_monthly_report() == {
		'user': 'test_user',
		'month': 'January',
		'income': 5000,
		'expenses': 2000,
		'savings': 1000,
		'investments': [investment]
	}


def test_report_manager():
	user = User('test_user', 'password', 'test_user@example.com')
	investment = Investment('test_investment', 10, 100, 150)
	report_manager = ReportManager()
	report = report_manager.create_report(user, 'January', 5000, 2000, 1000, [investment])

	assert report_manager.get_report('test_user', 'January') == report
