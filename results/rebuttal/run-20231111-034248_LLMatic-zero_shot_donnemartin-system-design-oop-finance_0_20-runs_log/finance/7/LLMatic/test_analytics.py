import pytest
from analytics import Analytics


def test_generate_monthly_report():
	analytics = Analytics()
	analytics.add_data('user1', {'month': 'January', 'spending': 1000})
	report = analytics.generate_monthly_report('user1')
	assert report == [{'month': 'January', 'spending': 1000}]


def test_generate_spending_habits():
	analytics = Analytics()
	analytics.add_data('user1', {'month': 'January', 'spending': 1000})
	report = analytics.generate_spending_habits('user1')
	assert report == [{'month': 'January', 'spending': 1000}]


def test_compare_year_on_year():
	analytics = Analytics()
	analytics.add_data('user1', {'year': 2020, 'spending': 12000})
	report = analytics.compare_year_on_year('user1')
	assert report == [{'year': 2020, 'spending': 12000}]
