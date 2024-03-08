import pytest
from transaction import Transaction

def test_add_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', 'expense')
	assert transaction.transactions['user1'][0]['amount'] == 100
	assert transaction.transactions['user1'][0]['category'] == 'groceries'
	assert transaction.transactions['user1'][0]['transaction_type'] == 'expense'

def test_categorize_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', 'expense')
	transaction.categorize_transaction('user1', 0, 'entertainment')
	assert transaction.transactions['user1'][0]['category'] == 'entertainment'

def test_classify_recurring_transactions():
	transaction = Transaction()
	transaction.add_transaction('user1', 100, 'groceries', 'expense')
	transaction.add_transaction('user1', 200, 'rent', 'expense', True)
	recurring_transactions = transaction.classify_recurring_transactions('user1')
	assert len(recurring_transactions) == 1
	assert recurring_transactions[0]['amount'] == 200
	assert recurring_transactions[0]['category'] == 'rent'
	assert recurring_transactions[0]['transaction_type'] == 'expense'
