import pytest
from analytics import Analytics


def test_generate_monthly_financial_report():
	analytics = Analytics('test_user')
	result = analytics.generate_monthly_financial_report()
	assert result['status'] == 'success'


def test_get_spending_habits():
	analytics = Analytics('test_user')
	result = analytics.get_spending_habits()
	assert result['status'] == 'success'


def test_get_financial_trends():
	analytics = Analytics('test_user')
	result = analytics.get_financial_trends()
	assert result['status'] == 'success'


def test_compare_year_on_year_data():
	analytics = Analytics('test_user')
	result = analytics.compare_year_on_year_data()
	assert result['status'] == 'success'
