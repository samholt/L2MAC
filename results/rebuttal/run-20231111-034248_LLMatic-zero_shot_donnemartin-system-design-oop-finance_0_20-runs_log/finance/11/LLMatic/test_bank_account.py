import pytest
from models import BankAccount
from data import Transaction


def test_bank_account():
	# Test linking bank account
	account = BankAccount.link_account('user1', 'Bank', '123456789')
	assert account.user_id == 'user1'
	assert account.bank_name == 'Bank'
	assert account.account_number == '123456789'

	# Test unlinking bank account
	BankAccount.unlink_account('user1')
	assert 'user1' not in BankAccount.accounts

	# Test importing transactions
	transactions = BankAccount.import_transactions('user1')
	assert transactions == [{'id': 1, 'amount': 100, 'category': 'groceries', 'recurring': False}]

