from account import Account
from transaction import Transaction
from datetime import datetime


def test_account():
	account = Account()
	transaction = Transaction(100, 'groceries', 'Grocery shopping', datetime(2022, 1, 1))
	account.transactions.append(transaction)
	account.update_balance()
	assert account.balance == 100
	assert len(account.transactions) == 1
	assert account.transactions[0].amount == 100
	assert account.transactions[0].category == 'groceries'
	assert account.transactions[0].date == datetime(2022, 1, 1)
