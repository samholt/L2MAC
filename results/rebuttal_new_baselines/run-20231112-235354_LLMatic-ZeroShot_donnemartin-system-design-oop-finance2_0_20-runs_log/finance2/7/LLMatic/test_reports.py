import pytest
from reports import Reports
from user import User

def test_reports():
	user = User('Test User', 'password')
	reports = Reports()
	reports.generate_monthly_summary(user)
	assert reports.get_report('monthly_summary') == 'Monthly summary for user: Test User'
	reports.generate_alerts(user)
	assert reports.get_report('alerts') == 'Alerts for user: Test User'
