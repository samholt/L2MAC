import pytest
from bank import Bank


def test_link_account():
	bank = Bank()
	bank.link_account('user1', '123456', 'Bank1')
	assert bank.accounts['user1'][0]['account_number'] == '123456'
	assert bank.accounts['user1'][0]['bank_name'] == 'Bank1'
	assert bank.accounts['user1'][0]['balance'] == 0


def test_import_transactions():
	bank = Bank()
	bank.link_account('user1', '123456', 'Bank1')
	bank.import_transactions('user1', '123456', [{'amount': 100}, {'amount': -50}])
	assert bank.accounts['user1'][0]['balance'] == 50


def test_update_balance():
	bank = Bank()
	bank.link_account('user1', '123456', 'Bank1')
	bank.update_balance('user1', '123456', 200)
	assert bank.accounts['user1'][0]['balance'] == 200
