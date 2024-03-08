import pytest
from transaction import Transaction

def test_add_transaction():
	transaction = Transaction()
	transaction.add_transaction('user1', {'amount': 100, 'category': 'groceries', 'recurring': False})
	assert transaction.transactions['user1'][0]['amount'] == 100

def test_categorize_transactions():
	transaction = Transaction()
	transaction.add_transaction('user1', {'amount': 100, 'category': 'groceries', 'recurring': False})
	transaction.add_transaction('user1', {'amount': 50, 'category': 'entertainment', 'recurring': False})
	categories = transaction.categorize_transactions('user1')
	assert len(categories['groceries']) == 1
	assert len(categories['entertainment']) == 1

def test_identify_recurring_transactions():
	transaction = Transaction()
	transaction.add_transaction('user1', {'amount': 100, 'category': 'groceries', 'recurring': True})
	transaction.add_transaction('user1', {'amount': 50, 'category': 'entertainment', 'recurring': False})
	recurring = transaction.identify_recurring_transactions('user1')
	assert len(recurring) == 1
