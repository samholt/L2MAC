import pytest
from analytics import Analytics


def test_generate_monthly_report():
	analytics = Analytics()
	assert analytics.generate_monthly_report('January') == 'No data for this month'


def test_visualize_spending():
	analytics = Analytics()
	assert analytics.visualize_spending('January') == 'No data for this month'


def test_compare_year_on_year():
	analytics = Analytics()
	assert analytics.compare_year_on_year('2020', '2021') == 'Data for one or both years not available'
