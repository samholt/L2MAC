import pytest
from bank_account import BankAccount


def test_link_bank_account():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', 'Bank1', '123456')
	assert bank_account.bank_accounts['user1'][0]['bank_name'] == 'Bank1'
	assert bank_account.bank_accounts['user1'][0]['account_number'] == '123456'
	assert bank_account.bank_accounts['user1'][0]['balance'] == 0


def test_import_transactions():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', 'Bank1', '123456')
	bank_account.import_transactions('user1', '123456', [{'amount': 100}, {'amount': -50}])
	assert bank_account.bank_accounts['user1'][0]['balance'] == 50


def test_update_balance():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', 'Bank1', '123456')
	bank_account.update_balance('user1', '123456', 200)
	assert bank_account.bank_accounts['user1'][0]['balance'] == 200
