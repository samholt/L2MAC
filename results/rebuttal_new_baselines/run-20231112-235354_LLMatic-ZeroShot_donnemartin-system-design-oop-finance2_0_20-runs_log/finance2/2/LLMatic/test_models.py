import pytest
from models.investment import Investment

def test_investment_model():
	investment = Investment('Test Account', 1000, {'stocks': 50, 'bonds': 50})

	# Test linking account
	investment.link_account('New Account')
	assert investment.account_name == 'New Account'

	# Test tracking performance
	assert investment.track_performance() == 1000

	# Test viewing asset allocation
	assert investment.view_asset_allocation() == {'stocks': 50, 'bonds': 50}
