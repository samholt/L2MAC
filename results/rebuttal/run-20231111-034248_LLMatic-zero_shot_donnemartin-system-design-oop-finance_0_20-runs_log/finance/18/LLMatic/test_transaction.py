from transaction import Transaction
from datetime import datetime, timedelta


def test_create_transaction():
	transaction = Transaction(100, 'Groceries', 'Grocery shopping')
	assert transaction.amount == 100
	assert transaction.category == 'Groceries'
	assert transaction.description == 'Grocery shopping'


def test_categorize_transaction():
	transaction = Transaction(100, 'Groceries', 'Grocery shopping')
	transaction.categorize_transaction('Bills')
	assert transaction.category == 'Bills'


def test_is_recurring():
	transaction1 = Transaction(100, 'Groceries', 'Grocery shopping')
	transaction2 = Transaction(200, 'Groceries', 'Grocery shopping', datetime.now() - timedelta(days=30))
	assert transaction1.is_recurring([transaction2])
