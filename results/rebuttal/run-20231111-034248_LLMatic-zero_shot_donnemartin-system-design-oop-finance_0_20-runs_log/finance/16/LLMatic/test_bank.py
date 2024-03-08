import pytest
from bank import BankAccount
from user import User
from transaction import Transaction


def test_link_account():
	user = User('test_user', 'password')
	account = BankAccount(user, '123456789')
	linked_account = BankAccount(user, '987654321')
	assert account.link_account(linked_account) == 'Account linked successfully'
	assert linked_account in account.linked_accounts


def test_import_transactions():
	user = User('test_user', 'password')
	account = BankAccount(user, '123456789')
	transactions = [Transaction(user, 100, 'groceries', 'expense'), Transaction(user, 200, 'salary', 'income')]
	assert account.import_transactions(transactions) == 'Transactions imported successfully'
	assert transactions == account.transactions


def test_update_balance():
	user = User('test_user', 'password')
	account = BankAccount(user, '123456789')
	transactions = [Transaction(user, 100, 'groceries', 'expense'), Transaction(user, 200, 'salary', 'income')]
	account.import_transactions(transactions)
	assert account.update_balance() == 'Balance updated successfully'
	assert account.balance == 300
