import pytest
from transaction import Transaction

def test_add_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', '2022-01-01')
	assert transaction.transactions['user1'][0]['amount'] == 100


def test_categorize_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', '2022-01-01')
	transaction_id = id(transaction.transactions['user1'][0])
	transaction.categorize_transaction('user1', transaction_id, 'entertainment')
	assert transaction.transactions['user1'][0]['category'] == 'entertainment'


def test_classify_recurring_transactions():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', '2022-01-01')
	transaction.add_transaction('user1', 100, 'groceries', '2022-01-02')
	transaction.add_transaction('user1', 200, 'groceries', '2022-01-03')
	transaction.add_transaction('user1', 100, 'groceries', '2022-01-04')
	recurring_transactions = transaction.classify_recurring_transactions('user1')
	assert len(recurring_transactions) == 1
