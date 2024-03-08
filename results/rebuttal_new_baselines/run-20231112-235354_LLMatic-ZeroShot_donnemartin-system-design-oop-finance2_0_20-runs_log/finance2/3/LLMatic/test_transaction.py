import pytest
from models.transaction import Transaction


def test_create_transaction():
	transaction = Transaction.create_transaction('user1', 100, 'groceries')
	assert transaction.user == 'user1'
	assert transaction.amount == 100
	assert transaction.category == 'groceries'


def test_get_user_transactions():
	Transaction.create_transaction('user1', 200, 'utilities')
	transactions = Transaction.get_user_transactions('user1')
	assert len(transactions) == 2
	assert transactions[0]['amount'] == 100
	assert transactions[1]['amount'] == 200


def test_categorize_transactions():
	Transaction.create_transaction('user1', 300, 'groceries')
	groceries_transactions = Transaction.categorize_transactions('user1', 'groceries')
	assert len(groceries_transactions) == 2
	assert groceries_transactions[0]['amount'] == 100
	assert groceries_transactions[1]['amount'] == 300
