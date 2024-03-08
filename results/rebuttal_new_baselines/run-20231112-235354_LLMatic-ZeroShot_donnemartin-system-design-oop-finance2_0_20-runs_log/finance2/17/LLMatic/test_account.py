import pytest
from account import Account

def test_account_creation():
	account = Account('Test Account', 1000)
	assert account.account_name == 'Test Account'
	assert account.balance == 1000


def test_buy_asset():
	account = Account('Test Account', 1000)
	account.buy_asset('Test Asset', 500)
	assert account.assets == {'Test Asset': 500}
	assert account.balance == 500


def test_sell_asset():
	account = Account('Test Account', 1000)
	account.buy_asset('Test Asset', 500)
	account.sell_asset('Test Asset', 200)
	assert account.assets == {'Test Asset': 300}
	assert account.balance == 700


def test_get_assets():
	account = Account('Test Account', 1000)
	account.buy_asset('Test Asset', 500)
	assert account.get_assets() == {'Test Asset': 500}


def test_get_performance():
	account = Account('Test Account', 1000)
	account.buy_asset('Test Asset', 500)
	assert account.get_performance() == 500
