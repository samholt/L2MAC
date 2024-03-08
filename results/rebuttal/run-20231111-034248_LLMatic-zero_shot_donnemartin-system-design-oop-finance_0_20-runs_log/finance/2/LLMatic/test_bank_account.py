import pytest
from bank_account import BankAccount


def test_link_bank_account():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', {'account_number': '123456', 'balance': 0, 'transactions': []})
	assert bank_account.bank_accounts['user1'][0]['account_number'] == '123456'


def test_import_transactions():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', {'account_number': '123456', 'balance': 0, 'transactions': []})
	bank_account.import_transactions('user1', [{'amount': 100, 'description': 'salary'}])
	assert bank_account.bank_accounts['user1'][0]['transactions'][0]['amount'] == 100


def test_update_account_balance():
	bank_account = BankAccount()
	bank_account.link_bank_account('user1', {'account_number': '123456', 'balance': 0, 'transactions': []})
	bank_account.import_transactions('user1', [{'amount': 100, 'description': 'salary'}])
	bank_account.update_account_balance('user1')
	assert bank_account.bank_accounts['user1'][0]['balance'] == 100
