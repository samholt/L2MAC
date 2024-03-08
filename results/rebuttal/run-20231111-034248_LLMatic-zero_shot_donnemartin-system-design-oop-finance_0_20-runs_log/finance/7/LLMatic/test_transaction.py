import pytest
from transaction import Transaction

def test_add_income():
	transaction = Transaction()
	transaction.add_income('user1', 1000, 'salary')
	assert transaction.transactions['user1'][0] == {'type': 'income', 'amount': 1000, 'category': 'salary'}

def test_add_expense():
	transaction = Transaction()
	transaction.add_expense('user1', 500, 'groceries')
	assert transaction.transactions['user1'][0] == {'type': 'expense', 'amount': 500, 'category': 'groceries'}

def test_categorize_transaction():
	transaction = Transaction()
	transaction.add_income('user1', 1000, 'salary')
	transaction.categorize_transaction('user1', 0, 'bonus')
	assert transaction.transactions['user1'][0]['category'] == 'bonus'

def test_identify_recurring_transactions():
	transaction = Transaction()
	transaction.add_income('user1', 1000, 'salary')
	transaction.add_income('user1', 1000, 'salary')
	assert transaction.identify_recurring_transactions('user1') == [{'type': 'income', 'amount': 1000, 'category': 'salary'}]
