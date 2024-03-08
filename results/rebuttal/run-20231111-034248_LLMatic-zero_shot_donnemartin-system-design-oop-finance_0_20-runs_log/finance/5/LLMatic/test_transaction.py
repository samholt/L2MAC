import pytest
from transaction import Transaction

def test_transaction():
	transaction = Transaction(100, 'Groceries', '2022-01-01', False, False)
	assert transaction.amount == 100
	assert transaction.category == 'Groceries'
	assert transaction.date == '2022-01-01'
	assert transaction.is_recurring == False
	assert transaction.is_deposit == False

	transaction.enter_transaction(200, 'Rent', '2022-02-01', True)
	assert transaction.amount == 200
	assert transaction.category == 'Rent'
	assert transaction.date == '2022-02-01'
	assert transaction.is_deposit == True

	transaction.categorize_transaction('Utilities')
	assert transaction.category == 'Utilities'

	transaction.check_recurring([Transaction(200, 'Utilities', '2022-02-01', False, True)])
	assert transaction.is_recurring == True
