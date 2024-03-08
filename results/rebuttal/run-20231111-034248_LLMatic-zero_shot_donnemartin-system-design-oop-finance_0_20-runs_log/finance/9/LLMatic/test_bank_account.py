import pytest
from bank_account import BankAccount, BankAccountManager
from transaction import Transaction


def test_bank_account():
	bank_account = BankAccount('123456789')
	assert bank_account.account_number == '123456789'
	assert bank_account.balance == 0
	assert bank_account.transactions == []

	bank_account.link_account('987654321')
	assert bank_account.account_number == '987654321'

	transactions = [Transaction('T1', 100.0, '2022-01-01', 'debit'), Transaction('T2', 50.0, '2022-01-02', 'credit')]
	bank_account.import_transactions(transactions)
	assert bank_account.transactions == transactions
	assert bank_account.balance == 50.0


def test_bank_account_manager():
	manager = BankAccountManager()
	assert manager.bank_accounts == {}

	manager.link_account('123456789')
	assert '123456789' in manager.bank_accounts

	transactions = [Transaction('T1', 100.0, '2022-01-01', 'debit'), Transaction('T2', 50.0, '2022-01-02', 'credit')]
	manager.import_transactions('123456789', transactions)
	assert manager.bank_accounts['123456789'].transactions == transactions
	assert manager.bank_accounts['123456789'].balance == 50.0

	manager.update_balance('123456789')
	assert manager.bank_accounts['123456789'].balance == 50.0
