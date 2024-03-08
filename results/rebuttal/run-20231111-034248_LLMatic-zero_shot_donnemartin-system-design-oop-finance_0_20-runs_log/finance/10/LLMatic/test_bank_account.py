import pytest
from bank_account import BankAccount

def test_link_account():
	bank_account = BankAccount()
	bank_account.link_account('123', 1000)
	assert bank_account.get_account('123') == {'balance': 1000, 'transactions': []}

def test_import_transactions():
	bank_account = BankAccount()
	bank_account.link_account('123', 1000)
	bank_account.import_transactions('123', [{'amount': 100, 'description': 'groceries'}, {'amount': -50, 'description': 'refund'}])
	assert bank_account.get_account('123') == {'balance': 1050, 'transactions': []}

def test_update_balance():
	bank_account = BankAccount()
	bank_account.link_account('123', 1000)
	bank_account.import_transactions('123', [{'amount': 100, 'description': 'groceries'}, {'amount': -50, 'description': 'refund'}])
	bank_account.update_balance('123')
	assert bank_account.get_account('123')['balance'] == 1050
