import pytest
from reports import Reports

def test_reports():
	reports = Reports()
	reports.add_data('January', 1000, 2000, 1500, 500)
	assert reports.generate_report('January') == {'expenses': 1000, 'incomes': 2000, 'budget': 1500, 'investments': 500}
	assert reports.generate_report('February') == 'No data for this month'
	assert reports.set_alert('January', 'High expenses') == 'Alert set'
	assert reports.set_alert('February', 'High expenses') == 'No data for this month to set an alert'
	assert reports.generate_report('January') == {'expenses': 1000, 'incomes': 2000, 'budget': 1500, 'investments': 500, 'alert': 'High expenses'}
