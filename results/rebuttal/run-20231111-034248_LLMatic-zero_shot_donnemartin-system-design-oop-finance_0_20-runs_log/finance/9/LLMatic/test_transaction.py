import pytest
from transaction import Transaction, TransactionManager
from datetime import datetime


def test_transaction():
	transaction = Transaction(1, 100, datetime.now(), 'expense')
	assert transaction.id == 1
	assert transaction.amount == 100
	assert transaction.type == 'expense'


def test_transaction_manager():
	manager = TransactionManager()
	manager.add_transaction(1, 100, datetime.now(), 'expense')
	assert manager.transactions[1].id == 1
	assert manager.transactions[1].amount == 100
	assert manager.transactions[1].type == 'expense'

	manager.delete_transaction(1)
	assert manager.get_transaction(1) == None
