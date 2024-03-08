import pytest
from investment import Investment


def test_investment():
	investment = Investment()

	# Test linking account
	investment.link_account('Account1', {'balance': 1000, 'assets': {'Stocks': 500, 'Bonds': 500}})
	assert investment.get_balance() == 1000
	assert investment.get_asset_allocation() == {'Stocks': 500, 'Bonds': 500}

	# Test tracking performance
	investment.track_performance('Account1', 10)
	assert investment.performance['Account1'] == 10

	# Test linking another account
	investment.link_account('Account2', {'balance': 2000, 'assets': {'Stocks': 1000, 'Bonds': 1000}})
	assert investment.get_balance() == 3000
	assert investment.get_asset_allocation() == {'Stocks': 1500, 'Bonds': 1500}
