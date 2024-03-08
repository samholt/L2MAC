import pytest
from investment import Investment
from account import Account


def test_investment_integration():
	investment = Investment()
	account = Account('Test Account', 1000)
	investment.integrate_account('Test Account', account)
	assert 'Test Account' in investment.accounts
	assert investment.balance == 1000


def test_investment_performance():
	investment = Investment()
	account = Account('Test Account', 1000)
	investment.integrate_account('Test Account', account)
	assert 'Test Account' in investment.performance


def test_investment_asset_allocation():
	investment = Investment()
	account = Account('Test Account', 1000)
	account.buy_asset('Test Asset', 500)
	investment.integrate_account('Test Account', account)
	assert investment.get_asset_allocation() == {'Test Asset': 500}
