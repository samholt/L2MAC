import pytest
from investment import Investment

def test_investment():
	investment = Investment({})
	assert investment.integrate_investment_account({'account': '123456'}) == 'Investment account integrated successfully'
	assert investment.track_investment_performance({'performance': 'good'}) == 'Investment performance tracked successfully'
	assert investment.track_investment_balance(1000) == 'Investment balance tracked successfully'
	assert investment.provide_asset_allocation_overview({'allocation': '50% stocks, 50% bonds'}) == 'Asset allocation overview provided successfully'
