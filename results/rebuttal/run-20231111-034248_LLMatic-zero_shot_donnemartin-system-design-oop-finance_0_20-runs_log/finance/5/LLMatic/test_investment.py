import pytest
from investment import Investment

def test_investment():
	investment = Investment('Tesla', 'Stock', 1000, 1000, 0)
	assert investment.investment_name == 'Tesla'
	assert investment.investment_type == 'Stock'
	assert investment.amount_invested == 1000
	assert investment.current_value == 1000
	assert investment.roi == 0

	investment.add_investment('Apple', 'Stock', 2000)
	assert investment.investment_name == 'Apple'
	assert investment.investment_type == 'Stock'
	assert investment.amount_invested == 2000
	assert investment.current_value == 2000
	assert investment.roi == 0

	investment.track_investment(2200)
	assert investment.current_value == 2200
	assert investment.roi == 0.1

	assert investment.alert_user() == 'Investment value is stable'

	investment.track_investment(2400)
	assert investment.current_value == 2400
	assert investment.roi == 0.2

	assert investment.alert_user() == 'Investment value has increased significantly'

	investment.track_investment(1600)
	assert investment.current_value == 1600
	assert investment.roi == -0.2

	assert investment.alert_user() == 'Investment value has decreased significantly'
