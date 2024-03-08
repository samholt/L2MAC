import pytest
from analytics import Analytics


def test_add_data():
	analytics = Analytics()
	analytics.add_data('user1', 'January', 100)
	assert analytics.data == {'user1': {'January': 100}}


def test_monthly_report():
	analytics = Analytics()
	analytics.add_data('user1', 'January', 100)
	assert analytics.monthly_report('user1') == {'January': 100}


def test_yearly_report():
	analytics = Analytics()
	analytics.add_data('user1', 'January', 100)
	analytics.add_data('user1', 'February', 200)
	assert analytics.yearly_report('user1') == 300


def test_compare_year_on_year():
	analytics = Analytics()
	analytics.add_data('user1', '2019', 100)
	analytics.add_data('user1', '2020', 200)
	assert analytics.compare_year_on_year('user1', '2019', '2020') == 100
