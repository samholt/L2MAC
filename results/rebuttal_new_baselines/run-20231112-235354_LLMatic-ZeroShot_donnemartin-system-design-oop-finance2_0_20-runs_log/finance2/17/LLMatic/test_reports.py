import pytest
from reports import Reports


def test_generate_financial_report():
	# Mocking a database
	database = {'1': {'balance': 1000, 'expenses': 500, 'income': 1500, 'alerts': {}}}
	reports = Reports(database)
	report = reports.generate_financial_report('1')
	assert report == {'balance': 1000, 'expenses': 500, 'income': 1500}


def test_customize_alerts():
	# Mocking a database
	database = {'1': {'balance': 1000, 'expenses': 500, 'income': 1500, 'alerts': {}}}
	reports = Reports(database)
	alerts = reports.customize_alerts('1', 'low_balance', 100)
	assert alerts == {'low_balance': 100}
